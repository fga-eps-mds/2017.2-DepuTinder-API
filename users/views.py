from django.shortcuts import render
from .models import Users
from .serializers import UsersSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from rest_framework.decorators import api_view
import requests, json

@api_view(['GET', 'POST'])
def users(request):

    if request.method == 'GET':
        users = Users.objects.all()
        if len(users) == 0:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = serializers.serialize('json', users)

            return Response(serializer, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        if request.data:
            user, created = Users.objects.get_or_create(
                userName = request.data['name'],
                userImage = '',
                userPassword = request.data['password'],
                userEmail = request.data['email'],
            )

            if created:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
