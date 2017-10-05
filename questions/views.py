from django.shortcuts import render
from .models import Questions
from .serializers import QuestionsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests, json

@api_view(['GET'])
def questions(request):
    questions = Questions.objects.all()

    if questions:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    else:
        serializer = QuestionsSerializer(questions)
        r = requests.get('https://api.myjson.com/bins/b43fx', serializer)
        data = json.loads(r.text)

        return Response(data, status=status.HTTP_201_CREATED)

