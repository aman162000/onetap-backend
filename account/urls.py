from django.urls import path, include
from .views import OnBoardingStatusAPIView, TeacherReteriveAPIView, CustomTokenView, TeacherListAPIView, CreatUserAPIView, AddPersonalInfoAPIView

urlpatterns = [
    path("auth/jwt/create/", CustomTokenView.as_view(), name="custom-token"),
    path("auth/", include("djoser.urls.jwt")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("reterive/", TeacherListAPIView.as_view(), name="teacher-list"),
    path("reterive/<str:uid>/", TeacherReteriveAPIView.as_view(),
         name="teacher-reterive"),
    path("register/", CreatUserAPIView.as_view(), name="student-register"),
    path("add-info/", AddPersonalInfoAPIView.as_view(), name="add-info"),
    path("check-status/", OnBoardingStatusAPIView.as_view(),
         name="onboarding-status")
]
