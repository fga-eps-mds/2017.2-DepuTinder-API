
from django.shortcuts import render
from .models import Question
from  propositions.models import Propositions
from .serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from rest_framework.decorators import api_view
import requests, json

@api_view(['GET', 'POST'])
def question(request):

    if request.method == 'GET':
        question = Question.objects.all()
        if len(question) == 0:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = serializers.serialize('json', question)

            return Response(serializer, status=status.HTTP_200_OK)

    elif request.method == 'POST':

        if request.data:
            propo = Propositions.objects.get(propositionTitle = request.data['propositionFK'])
            print(propo)
            question, created = Question.objects.get_or_create(
                questionTitle = request.data['questionTitle'],
                questionSubtitle = request.data['questionSubtitle'],
                questionDescription = request.data['questionDescription'],
                questionAuthor = request.data['questionAuthor'],
                proposition = propo,
            )
            
            if created:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
