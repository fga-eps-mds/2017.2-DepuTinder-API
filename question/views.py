
from django.shortcuts import render
from .models import Question
from questionnaire.models import Questionnaire
from  propositions.models import Propositions
from .serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from rest_framework.decorators import api_view
from django.http import JsonResponse
import requests, json

@api_view(['GET', 'POST'])
def question(request):

    if request.method == 'GET':
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return JsonResponse(serializer.data, safe=False)

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

@api_view(['PUT'])
def updateQuestion(request):
    questions = Question.objects.all()
    currentQuestionnaire = Questionnaire.objects.get(id=1)
    dontQuestionnaire = Questionnaire.objects.get(id=2)
    questionnaire = request.data['questionnaireFK']

    for question in questions:
        for questionInQuestionnaire in questionnaire:
            questionRequest = Question.objects.get(questionTitle=question.questionTitle)
            print(questionRequest.questionTitle)
            if question.questionTitle is questionInQuestionnaire['questionTitle']:
                questionRequest.questionnaireFK = questionRequest.questionnaireFK._replace(currentQuestionnaire)
                questionRequest.save()
            else:
                # questionRequest.questionnaireFK = dontQuestionnaire
                questionRequest.questionnaireFK = questionRequest.questionnaireFK._replace(dontQuestionnaire)
                questionRequest.save()


    return JsonResponse({"status": 500, "message": "Questão não existe!"}, status=status.HTTP_200_OK)
