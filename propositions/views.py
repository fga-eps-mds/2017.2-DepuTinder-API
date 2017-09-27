from django.shortcuts import render
from .models import Propositions
from .serializers import PropositionsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests, json

@api_view(['GET'])
def propositions(request):
    propositions = Propositions.objects.all()

    if propositions:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    else:
        serializer = PropositionsSerializer(propositions)
        r = requests.get('https://api.myjson.com/bins/m7f4x', serializer)
        data = json.loads(r.text)

        return Response(data, status=status.HTTP_201_CREATED)
