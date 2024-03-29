from rest_framework import serializers
from rest_framework.response import Response
from .models import UserModel
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    lastname = serializers.CharField()
    email = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validate_data):
        return UserModel.objects.create(**validate_data)
