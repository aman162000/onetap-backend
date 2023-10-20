from account.models import Teacher, User, Subject, Department
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import SubjectSerializer, DepartmentSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.models import Teacher, Student, Subject


class SubjectListAPIView(ListAPIView):

    serializer_class = SubjectSerializer

    def get_queryset(self):
        teacher_obj = Teacher.objects.get(user=self.request.user)

        return teacher_obj.subject.all()


class DepartmentListAPIView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class StudentSummaryAPIView(RetrieveAPIView):
    pass


class TotalEnrolledStudentAPIView(APIView):

    def get(self, request, uid):
        user = request.user
        subject = Subject.objects.get(uid=uid)
        count = subject.student_set.count()
        return Response({"count": count}, status=status.HTTP_200_OK)
