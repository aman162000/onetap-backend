from rest_framework import serializers
from .models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = "__all__"
        validators = []


class SubjectAttendanceSerializer(serializers.Serializer):
    uid = serializers.UUIDField()
    subject_name = serializers.CharField()
    total_attendance = serializers.IntegerField()
    total_classes = serializers.IntegerField()


class UserAttendanceSerializer(serializers.Serializer):
    name = serializers.CharField()
    overall_attendance = serializers.DecimalField(
        decimal_places=5, max_digits=5)
    classes_attended = serializers.IntegerField()
    leaves_available = serializers.IntegerField()
    subject_wise = SubjectAttendanceSerializer(many=True)


class StudentAttendanceSerializer(serializers.Serializer):
    prn = serializers.IntegerField()
    student_name = serializers.CharField()
    is_present = serializers.BooleanField()


class AggregatedAttendanceSerializer(serializers.Serializer):
    uid = serializers.UUIDField()
    date = serializers.DateTimeField()
    subject = serializers.CharField()
    taken_by = serializers.CharField()
