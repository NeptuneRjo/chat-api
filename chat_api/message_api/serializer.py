from rest_framework import serializers
from .models import Message
from user_api.serializer import AccountSerializer


class MessageSerializer(serializers.ModelSerializer):
    read_by = AccountSerializer(many=True)

    class Meta:
        model = Message
        fields = ['uuid', 'contents', 'read_by']
