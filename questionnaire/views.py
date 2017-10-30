from django.shortcuts import render
from .models import Questionnaire
from .serializers import QuestionnaireSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests, json

@api_view(['GET'])
def questionnaire(request):
    questionnaire = Questionnaire.objects.all()

    if questionnaire:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    else:
        serializer = QuestionnaireSerializer(questionnaire, many=True)
        r = requests.get('http://myjson.com/nc619', serializer)
        data = json.loads(r.text)

        return Response(data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def answeredQuestions(request):
    if(request.data):
        print(request.data)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
