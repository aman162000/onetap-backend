from django.urls import path
from beacon.consumers import BeaconConsumer
from attendance.consumers import AttendanceConsumer

websocket_urlpatterns = [
    path("ws/data/", BeaconConsumer.as_asgi()),
    path("ws/attendance/", AttendanceConsumer.as_asgi())
]
