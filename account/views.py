from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from django.shortcuts import get_object_or_404
from .models import Teacher, User, Student, Department
from .serializers import TeacherSerializer, UserSerializer, CustomTokenObtainSerializer, StudentSerializer
# Create your views here.


class CustomTokenView(TokenObtainPairView):
    def post(self, request, **kwargs):
        user = get_object_or_404(User, email=request.data["email"])
        if user.is_student:
            student = Student.objects.get(user=user)
            if student.registerd_device == request.data["device_id"]:
                return super().post(request, **kwargs)
            else:
                return Response({
                    "detail": "Device is not same as registerd device"
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return super().post(request, **kwargs)


class TeacherListAPIView(ListAPIView):
    lookup_field = "uid"
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class TeacherReteriveAPIView(RetrieveAPIView):
    lookup_field = "uid"
    lookup_url_kwarg = "uid"
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class CreatUserAPIView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        request.data["is_student"] = True
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            token_data = {
                "email": request.data["email"],
                "password": request.data["password"]
            }
            token_serializer = CustomTokenObtainSerializer(data=token_data)
            token_serializer.is_valid(raise_exception=True)
            return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddPersonalInfoAPIView(CreateAPIView):

    serializer_class = StudentSerializer

    def get_object(self, request):
        return User.objects.get(email=request.user)

    def create(self, request, *args, **kwargs):
        user = self.get_object(request)
        department = Department.objects.get(uid=request.data["department"])
        serializer = self.get_serializer(data=request.data)
        request.data["user"] = user.pk
        request.data["enrolled_subjects"] = None
        request.data["department"] = department.pk
        if serializer.is_valid():
            serializer.save()
            user.onboarding_completed = True
            user.save()
            return Response({"message": "details add successfully"}, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OnBoardingStatusAPIView(RetrieveAPIView):

    def get(self, request, *args, **kwargs):

        return Response({"status": request.user.onboarding_completed}, status=status.HTTP_200_OK)
