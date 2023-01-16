from django.db import models
from user_api.models import Account

from chat_api.utils import uuid_generator
# Create your models here.


class Message(models.Model):
    uuid = models.CharField(max_length=6, null=True, blank=True, unique=True)
    contents = models.CharField(max_length=120)
    read_by = models.ManyToManyField(Account)

    def __str__(self):
        return self.uuid

    def save(self):
        if not self.uuid:
            # Generate UUID and check db. If exists, try again.
            self.uuid = uuid_generator()

            while Message.objects.filter(uuid=self.uuid).exists():
                self.uuid = uuid_generator()

        super(Message, self).save()

    def read_by_list(self):
        read_by = []

        for user in self.read_by.all():
            read_by.append(user)

        return read_by
