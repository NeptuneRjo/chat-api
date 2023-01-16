from rest_framework import serializers

from .models import Room

from user_api.serializer import AccountSerializer
from message_api.serializer import MessageSerializer


class RoomSerialize(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)
    online_users = AccountSerializer(many=True)
    all_users = AccountSerializer(many=True)

    class Meta:
        model = Room
        fields = ['uuid', 'messages', 'online_users', 'all_users']
