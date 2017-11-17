from django.shortcuts import render
from .models import Users
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import UsersSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from rest_framework.decorators import api_view
from django.http import JsonResponse
import requests, json
from users.models import Users

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def users(request):

    #method to GET all users from API
    if request.method == 'GET':
        users = Users.objects.all()

        seri = serializers.serialize('json', list(users))

        if not users:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            return JsonResponse(seri, safe=False)

    #method to POST a new User in API
    elif request.method == 'POST':
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

    #method to update an user from API
    elif request.method == 'PUT':
        u = User.objects.get(email=request.data['userEmail'])
        user_authenticate = authenticate(username=u.username, password=request.data['userPassword'])
        user = Users.objects.get(user=user_authenticate.id)

        if user is not None:
            seri = {
                "userName": user.user.username,
                "userEmail": user.user.email,
                "userImage": user.userImage,
            }

            return JsonResponse(seri)
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if request.data:
            print(request.data)
            deleteUser = User.objects.get(email=request.data['userEmail']).delete()
            return Response(status=status.HTTP_200_OK)
