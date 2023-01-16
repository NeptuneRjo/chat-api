from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Room
from user_api.models import Account
from message_api.models import Message


@api_view(['GET', ])
def get_room(request):
    if request.method == 'GET':
