from rest_framework import serializers
from .models import Teacher, Subject, Department, User, Student
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        depth = 2
        exclude = ("user",)


class CustomTokenObtainSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["user_type"] = "teacher" if user.is_teacher else "student"
        token["email"] = user.email
        return token


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("email", "password", "is_student")

    def create(self, validated_data):
        user = User(
            email=validated_data['email']
        )
        user.is_student = validated_data["is_student"]
        user.set_password(validated_data['password'])
        user.save()
        return user


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        exclude = ("enrolled_subjects",)

    def create(self, validated_data):
        student = Student.objects.create(**validated_data)
        return student
