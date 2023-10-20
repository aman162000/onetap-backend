from django.dispatch import receiver
from django.db.models.signals import post_save
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Attendance
from beacon.models import Beacon


@receiver(post_save, sender=Attendance)
def attendance_update(sender, instance, **kwargs):
    data = {
        "name": f"{instance.student.first_name} {instance.student.last_name}",
        "prn": instance.student.prn_no,
        "image": instance.student.image.url
    }
    # Modify this to access the lecturer identifier
    user_uid = Beacon.objects.get(uid=instance.beacon).lecturer.user.uid
    # Send the update to the specific user's WebSocket channel
    channel_layer = get_channel_layer()
    user_channel_name = f"user_{user_uid}"
    async_to_sync(channel_layer.group_send)(
        user_channel_name,
        {
            "type": "attendance_updated",
            "data": data,
        },
    )
