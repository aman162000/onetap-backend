from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(_("email address"), blank=False, unique=True)

    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email


class Department(BaseModel):
    department_name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self) -> str:
        return self.department_name


class Teacher(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    deptartment = models.ManyToManyField(Department)

    def __str__(self) -> str:
        return self.user.email


class Subject(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Student(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    prn_no = models.PositiveBigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    year = models.PositiveIntegerField()
    enrolled_subjects = models.ManyToManyField(Subject)

    def __str__(self) -> str:
        return self.user.email
