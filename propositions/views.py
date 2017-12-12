from django.shortcuts import render
from .models import Propositions
from .serializers import PropositionsSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
import requests, json

@api_view(['GET'])
def PropositionsView(request):
        #Propositions.objects.all().delete()
        propositions = Propositions.objects.all()
        serializer = PropositionsSerializer(propositions, many=True)
        return JsonResponse(serializer.data, safe=False)
