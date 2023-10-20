from rest_framework import serializers
from account.models import Subject, Department


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        exclude = ("id", "created_at", "updated_at",)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        exclude = ("id", "created_at", "updated_at",)
