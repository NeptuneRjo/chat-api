from django.db import models
from django.contrib.auth.models import User

from room_api.models import Room


# Create your models here.


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE),
    rooms = models.ManyToManyField(Room)

    def __str__(self):
        return self.user.username

    def room_list(self):
        room_list = []

        for room in self.rooms.all():
            room_list.append(room)

        return room_list
