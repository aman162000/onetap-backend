from django.urls import path
from .views import BeaconCreateAPIView

urlpatterns = [
    path("create/", BeaconCreateAPIView.as_view())
]
