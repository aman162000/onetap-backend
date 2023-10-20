from rest_framework import serializers
from .models import Beacon
from account.models import Subject


class BeaconSerializer(serializers.ModelSerializer):

    class Meta:
        model = Beacon
        fields = "__all__"
