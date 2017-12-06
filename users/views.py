from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core import serializers
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests, json
from .models import Users
from .serializers import UsersSerializer


@api_view(['GET'])
def getUsers(request):
    #method to GET all users from API
    if request.method == 'GET':
        users = User.objects.all()

        users_serialization = serializers.serialize('json', list(users))

        if not users:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            return JsonResponse(users_serialization, safe=False)

@api_view(['POST'])
def createUser(request):
    if request.data:
        user = User.objects.filter(email=request.data['userEmail'])
        if len(user) > 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            user = User.objects.create_user(request.data['userName'], request.data['userEmail'], request.data['userPassword'])
            user.save()
            users, created = Users.objects.get_or_create(
                user = user,
                userImage = request.data['userImage'],
            )
            if created:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def userLogin(request):
    requested_user = User.objects.filter(email=request.data['userEmail'])

    if not requested_user:
        return JsonResponse({"status": 500, "message": "Email não existe!"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        user_authenticate = authenticate(username=requested_user[0].username, password=request.data['userPassword'])

        if user_authenticate is not None:
            user = Users.objects.get(user=user_authenticate.id)
            user_serialization = {"data": {
                                   "userName": user.user.username,
                                   "userEmail": user.user.email,
                                   "userImage": user.userImage,
                                    },
                                  "status": 200,
                                  "message": "Login Realizado com Sucesso   !"
                                  }

            return JsonResponse(user_serialization)
        else:
            return JsonResponse({"status": 400, "message": "Email ou senha incorretos!"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateUser(request):
    requested_user = User.objects.filter(email=request.data['oldUserEmail'])

    if not requested_user:
        return JsonResponse({"status":500, "message": "Email não existe!"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        user_authenticate = authenticate(username=requested_user[0].username, password=request.data['oldUserPassword'])
        if user_authenticate is not None:
            user = Users.objects.get(user=user_authenticate.id)
            requested_user[0].username = request.data['userName']
            requested_user[0].email = request.data['userEmail']
            if(request.data['userPassword'] != ''):
                requested_user[0].set_password(request.data['userPassword'])
            requested_user[0].save()
            return JsonResponse({"status":400, "message": "Email ou senha incorretos"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({"status":400, "message": "Email ou senha incorretos"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteUser(request):
    if request.data:
        deleteUser = User.objects.get(email=request.data['userEmail']).delete()
        return Response(status=status.HTTP_200_OK)
