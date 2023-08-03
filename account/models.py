from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import BaseModel

# Create your models here.


class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class Teacher(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Subject(BaseModel):
    name = models.CharField(max_length=255)


class Student(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    prn_no = models.PositiveBigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    year = models.PositiveIntegerField()
    enrolled_subjects = models.ManyToManyField(Subject)
