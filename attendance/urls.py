from django.urls import path
from .views import AttendanceAPIView, UserAttendanceView, TeacherAttendanceView

urlpatterns = [
    path("mark/", AttendanceAPIView.as_view(), name="mark-attendace"),
    path("user-attendance/", UserAttendanceView.as_view(), name="user-attendace"),
    path("attendance-by-subject/", TeacherAttendanceView.as_view(), name="attendace")
]
