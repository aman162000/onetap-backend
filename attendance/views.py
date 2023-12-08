from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from .serializers import AttendanceSerializer, UserAttendanceSerializer, AggregatedAttendanceSerializer
from .models import Attendance
from rest_framework import status
from beacon.models import Beacon
from account.models import Student, Teacher
from rest_framework.response import Response
from django.db.models import Count, Q, F
# Create your views here.


def get_total_leave(current_attendance, total_attendance):
    return ((current_attendance - 0.75) * total_attendance)/0.25


def get_attendance_data(user):
    student = Student.objects.get(user=user.pk)
    enrolled_subjects = student.enrolled_subjects.all()
    data = []
    for subject in enrolled_subjects:
        subjectwise_data = {
            "uid": subject.uid,
            "subject_name": subject.name,
            "total_attendance": 0,
            "total_classes": subject.total_lecture,
        }

        attendances = Attendance.objects.filter(
            subject=subject, student=student)
        total_attendance = attendances.filter(is_present=True).count()
        subjectwise_data["total_attendance"] = total_attendance
        data.append(subjectwise_data)

    total_attendance = sum([subject["total_attendance"] for subject in data])
    total_classes = sum([subject["total_classes"] for subject in data])

    if total_classes > 0:
        overall_percentage = (total_attendance/total_classes)
    else:
        overall_percentage = 0
    user_data = {
        "name": student.first_name,
        "overall_attendance": overall_percentage,
        "classes_attended": total_attendance,
        "subject_wise": data,
        "leaves_available": 0 if overall_percentage <= 0.75 else get_total_leave(overall_percentage, total_attendance)
    }

    return user_data


def get_subject_attendance_data(teacher):

    subjects_taught = teacher.subject.prefetch_related('attendance_set').all()
    subject_data = []

    for subject in subjects_taught:
        attendance_records = subject.attendance_set.all()
        subject_attendance = attendance_records.first()
        attendance_date = subject_attendance.created_at if subject_attendance else None

        subject_info = {
            'uid': subject.uid,
            'date': attendance_date,
            'subject': subject.name,
            "taken_by": subject_attendance.taken_by.full_name
        }

        subject_data.append(subject_info)
    return subject_data


class AttendanceAPIView(CreateAPIView):

    serializer_class = AttendanceSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        beacon = Beacon.objects.get(minor_value=request.data["beacon"])
        request.data["is_present"] = True
        request.data["student"] = Student.objects.get(user=request.user.pk).pk
        request.data["subject"] = beacon.subject.pk
        serializer = self.get_serializer(data=request.data)
        request.data["beacon"] = str(beacon.uid)
        request.data["taken_by"] = beacon.lecturer.pk
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Attendance marked successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAttendanceView(APIView):
    def get(self, request):
        user = request.user
        data = get_attendance_data(user)

        serializer = UserAttendanceSerializer(data)

        return Response(serializer.data)


class TeacherAttendanceView(ListAPIView):
    def get(self, request):
        teacher = Teacher.objects.get(user=request.user)

        subjects_with_totals = get_subject_attendance_data(teacher)

        serializer = AggregatedAttendanceSerializer(
            subjects_with_totals, many=True)

        return Response(serializer.data)
