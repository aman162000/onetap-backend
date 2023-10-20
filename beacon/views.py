from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import BeaconSerializer
from account.models import Teacher, User, Subject
from .models import Beacon
from djoser.permissions import permissions
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class BeaconCreateAPIView(CreateAPIView):
    serializer_class = BeaconSerializer

    def create(self, request, *args, **kwargs):
        if not request.user.is_teacher:
            return Response({"message": "Not allowed"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        request.data["lecturer"] = Teacher.objects.get(user=request.user).pk
        request.data["subject"] = Subject.objects.get(
            uid=request.data["subject"]).pk
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
