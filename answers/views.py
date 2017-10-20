from django.shortcuts import render
from .models import Answers
from .serializers import AnswersSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests, json

@api_view(['GET','POST'])
def answers(request):
    if request.method == 'GET':
        answers = Answers.objects.all()
        if answers:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = AnswersSerializer(answers)
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = AnswersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
