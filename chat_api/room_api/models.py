from django.db import models
from message_api.models import Message
from user_api.models import Account

from chat_api.utils import uuid_generator


class Room(models.Model):
    uuid = models.CharField(max_length=6, null=True, blank=True, unique=True)
    messages = models.ManyToManyField(Message)
    online_users = models.ManyToManyField(Account)
    all_users = models.ManyToManyField(Account)

    def __str__(self):
        return self.uuid

    def save(self):
        if not self.uuid:
            # Generate UUID and check db. If exists, try again.
            self.uuid = uuid_generator()

            while Room.objects.filter(uuid=self.uuid).exists():
                self.uuid = uuid_generator()

        super(Room, self).save()

    def message_list(self):
        message_list = []

        for message in self.messages.all():
            message_list.append(message)

        return message_list

    def online_list(self):
        online_users = []

        for user in self.online_users.all():
            online_users.append(user)

        return online_users

    def users_list(self):
        users = []

        for user in self.all_users.all():
            users.append(user)

        return users
