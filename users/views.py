from django.shortcuts import render
from .models import Users
from .serializers import UsersSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from rest_framework.decorators import api_view
from cryptography.fernet import Fernet
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

            key = b'8YECmO6MCuZ0Lm887BkLlhqF_SvVb58TvbPohNfTwrk='
            cipher_suite = Fernet(key)

            user, created = Users.objects.get_or_create(
                userName = request.data['name'],
                userImage = '',
                userPassword = cipher_suite.encrypt(request.data['password'].encode('UTF-8')),
                userEmail = request.data['email'],
            )

            if created:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def login(request):

    email = request.GET.get('userEmail')
    password = request.GET.get('userPassword')

    key = b'8YECmO6MCuZ0Lm887BkLlhqF_SvVb58TvbPohNfTwrk='
    cipher_suite = Fernet(key)

    try:
        user = Users.objects.get(userEmail=email)
    except:
        return Response({"error": "Email not found"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        userPassword = user.userPassword
        userPassword = cipher_suite.decrypt(userPassword.encode('UTF-8'))
        userPassword = userPassword.decode('UTF-8')

        if userPassword == password:
            response = {"userName": user.userName,
                       "userImage": user.userImage,
                       "userEmail": user.userEmail,
                       }

            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid Password"}, status=status.HTTP_400_BAD_REQUEST)
