from django.shortcuts import render
from .models import Users
from .serializers import UsersSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests, json

@api_view(['GET'])
def usersGet(request):
    users = Users.objects.all()

    if users:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    else:
        serializer = UsersSerializer(users)
        userData = {
            "data": [
                {"userName": "Amanda", "userEmail":"amandalust@gmail.com", "userPassword":"rolezinho", "userImage":" ", "answeredQuestions": "1"}
            ],
        }

        return Response(userData, status=status.HTTP_200_OK)

@api_view(['POST'])
def usersPost(request):
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
