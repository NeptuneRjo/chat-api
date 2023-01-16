from rest_framework import serializers

from room_api.serializer import RoomSerialize
from .models import Account
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class AccountSerializer(serializers.Serializer):
    user = UserSerializer()
    rooms = RoomSerialize(many=True)

    class Meta:
        model = Account
        fields = ['user', 'rooms']
