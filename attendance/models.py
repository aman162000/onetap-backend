from core.models import BaseModel
from account.models import Student, Subject
from django.db import models

# Create your models here.


class Attendance(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)
