
from django.shortcuts import render
from .models import Question
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
    q = Question.objects.filter(questionTitle=request.data['questionTitle'])

    if not q:
        return JsonResponse({"status": 500, "message": "Questão não existe!"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        questionn = Questionnaire.objects.get(questionnaire = request.data['questionnaireFK'])
        question_authenticate = authenticate(questionTitle=q[0].questionTitle, questionnaire=questionn)
        if question_authenticate is not None:
            question = Question.objects.get(question=question_authenticate.id)
            q[0].questionn = request.data['questionnaireFK']
            print(request.data['questionnaireFK'])
            q[0].save()
            print(q[0].questionnaire)
            return JsonResponse({"status":400, "message": "Nao foi possivel salvar"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({"status":400, "message": "Nao foi possivel salvar"}, status=status.HTTP_400_BAD_REQUEST)
