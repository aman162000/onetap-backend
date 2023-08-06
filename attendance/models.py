from core.models import BaseModel
from account.models import Student, Subject
from django.db import models

# Create your models here.


class Attendance(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)

    class Meta:
        unique_together = ["student", "subject"]

    @classmethod
    def mark_attendance(cls, student, subject, is_present=False):
        """
        Method to create or mark an attendance record for student in a subject.
        """
        if subject in student.enrolled_subjects.all():

            return cls.objects.create(student=student, subject=subject, is_present=is_present)
        else:
            raise ValueError(
                "Student is not enrolled in the provided subject.")

    def update_attendance(self, is_present):
        """
        Method to update attendance status for this attendance record
        """
        self.is_present = is_present
        self.save()

    @classmethod
    def get_attendance_records_for_student(cls, student):
        """
        Method to reterive all attendance record for specific student
        """
        return cls.objects.filter(student=student)

    @classmethod
    def get_attendance_records_for_subject(cls, subject):
        """
        Method to reterive all attendance record for specific subject
        """
        return cls.objects.filter(subject=subject)

    @classmethod
    def calculate_attendance_statistics(cls, subject, student):
        """
        Method to calculate attendance statistics for a specific student and subject.
        """

        total_classes = cls.objects.filter(
            subject=subject, student=student).count()
        classes_attended = cls.objects.filter(
            subject=subject, student=student, is_present=True).count()
        classes_missed = total_classes - classes_attended
        if total_classes != 0:
            attendance_percentage = (
                classes_attended / total_classes) * 100
        else:
            attendance_percentage = 0

        return {
            'total_classes': total_classes,
            'classes_attended': classes_attended,
            'classes_missed': classes_missed,
            'attendance_percentage': attendance_percentage,
        }
