from django.shortcuts import render
from .models import Users
from .serializers import UsersSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests, json

@api_view(['GET'])
def users(request):
    users = Users.objects.all()

    if users:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    else:
        serializer = UsersSerializer(users)
        userData = { 
        	"data": [
        		{"userName": "Amanda", "userEmail":"amandalust@gmail.com", "userPassword":"rolezinho", "userImage":" "}
        	],
    	}

        return Response(userData, status=status.HTTP_200_OK)
