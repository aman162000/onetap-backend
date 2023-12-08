import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Beacon
from account.models import Student
from attendance.models import Attendance
from channels.db import database_sync_to_async


class BeaconConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()

        await self.send(text_data=json.dumps({
            "type": "websocket.send",
            "data": await self.fetch()
        }))

    @database_sync_to_async
    def fetch(self):
        user = self.scope["user"]
        data = {}
        if user.is_authenticated:
            beacon = Beacon.objects.get(
                minor_value=int(self.scope["minor_value"]))
            student = Student.objects.get(user=user)

            if student.enrolled_subjects.contains(beacon.subject) and not Attendance.objects.filter(student=student.pk, subject=beacon.subject.pk, beacon=beacon.uid).exists():
                data = {"subject": beacon.subject.name,
                        "beacon_id": beacon.minor_value,
                        "lecturer": f"{beacon.lecturer.first_name} {beacon.lecturer.last_name}"}
        else:
            data = {"error": "User is not authenticated"}

        return data
