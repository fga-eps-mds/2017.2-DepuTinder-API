from django.shortcuts import render
from .models import Questionnaire
from .serializers import QuestionnaireSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
import requests, json

@api_view(['GET', 'POST'])
def questionnaire(request):

    if request.method == 'GET':
        questionnaire = Questionnaire.objects.all()

        if len(questionnaire):
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = QuestionnaireSerializer(questionnaire, many=True)
            return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':

        if request.data:

            questionnaire, created = Questionnaire.objects.get_or_create(
                questionsTotal = request.data['questionsTotal'],
            )

            if created:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
