from django.db import models
from core.models import BaseModel
from account.models import Teacher, Subject, Student

# Create your models here.


class Beacon(BaseModel):
    minor_value = models.IntegerField(
        null=False, blank=False, verbose_name="Subject Id", help_text="The unique identifier for the subject associated with this beacon.")
    lecturer = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, help_text="The lecturer associated with this beacon.")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,
                                help_text="The subject associated with this beacon.")

    class Meta:
        verbose_name = "Beacon"
        verbose_name_plural = "Beacons"

    def __str__(self):
        """
        Returns a string representation of the Beacon.
        """
        return f"Beacon for Subject {self.minor_value} - Lecturer: {self.lecturer}"

    def get_subject_name(self, minor_value):
        """
        Returns the name of the associated subject.
        """
        self.obj = self.objects.get(minor_value=minor_value)
        return self.obj.subject.name

    def get_lecturer_name(self):
        """
        Returns the name of the associated lecturer.
        """
        return f"{self.lecturer.first_name} {self.lecturer.last_name}"

    def save(self, *args, **kwargs):
        """
        Custom save method to perform any necessary actions before saving.
        """
        # You can add custom logic here before saving the object.
        super(Beacon, self).save(*args, **kwargs)

    def calculate_total_students_enrolled(self):
        """
        Calculates and returns the total number of students enrolled in the associated subject.
        """
        # Assuming there's a ManyToManyField or ForeignKey relationship between Subject and Student.
        # You should modify this logic according to your actual model structure.
        total_students = Student.objects.filter(
            enrolled_subjects=self.subject).count()
        return total_students
