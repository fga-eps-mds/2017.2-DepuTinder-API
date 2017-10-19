from django.shortcuts import render
from .models import Users
from .serializers import UsersSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests, json
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

@api_view(['GET', 'POST'])
def users(request):
    users = Users.objects.all()

    #GET
    if request.method == 'GET':    
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
    
    #POST
    else:
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


