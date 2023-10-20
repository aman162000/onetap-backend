from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.hashers import make_password
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _
# Create your models here.


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser, BaseModel):
    email = models.EmailField(_("email address"), blank=False, unique=True)
    username = None
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    onboarding_completed = models.BooleanField(default=False)  # New field
    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email


class Department(BaseModel):
    department_name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self) -> str:
        return self.department_name


class Subject(BaseModel):
    name = models.CharField(max_length=255)
    total_lecture = models.IntegerField(
        null=False, default=0, verbose_name="Total lectures")

    def __str__(self) -> str:
        return self.name


class Teacher(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    deptartment = models.ManyToManyField(Department)
    subject = models.ManyToManyField(Subject)

    def __str__(self) -> str:
        return self.user.email

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Student(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="user_image", default="", null=True)
    prn_no = models.PositiveBigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    year = models.PositiveIntegerField()
    enrolled_subjects = models.ManyToManyField(Subject, blank=True, null=True)
    registerd_device = models.CharField(max_length=255, null=False, default="")
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.email

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
