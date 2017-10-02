from django.shortcuts import render
from .models import Votings
from .serializers import VotingsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests, json

@api_view(['GET'])
def votings(request):
    votings = Votings.objects.all()

    if votings:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    else:
        serializer = VotingsSerializer(votings)
        r = requests.get('https://api.myjson.com/bins/17w6e1', serializer)
        data = json.loads(r.text)

        return Response(data, status=status.HTTP_201_CREATED)
