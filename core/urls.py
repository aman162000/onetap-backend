from django.urls import path
from .views import SubjectListAPIView, DepartmentListAPIView, TotalEnrolledStudentAPIView

urlpatterns = [
    path("department/", DepartmentListAPIView.as_view(), name="department-list"),
    path("subject/", SubjectListAPIView.as_view(), name="subject-list"),
    path("enrolled/students/<str:uid>/", TotalEnrolledStudentAPIView.as_view(),
         name="total-enrolled-students")
]
