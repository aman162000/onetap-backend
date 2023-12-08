import json
from channels.generic.websocket import AsyncWebsocketConsumer
from account.models import User, Student
from channels.exceptions import StopConsumer

class AttendanceConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        user = self.scope.get("user")
        if user is None:
            await self.close()
        else:
            # Create a unique WebSocket channel name for the user
            user_group_name = f"user_{user.uid}"
            await self.channel_layer.group_add(
                user_group_name, self.channel_name)
            await self.accept()

    async def disconnect(self, close_code):
        user = self.scope.get("user")

        if user is not None:
            # Remove the user from the group when they disconnect
            user_group_name = f"user_{user.uid}"
            await self.channel_layer.group_discard(user_group_name, self.channel_name)

            raise StopConsumer

    async def update_attendance(self, event):
        await self.send(json.dumps(event))

    async def attendance_updated(self, event):
        await self.send(json.dumps(event["data"]))
