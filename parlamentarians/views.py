from django.shortcuts import render
from .models import Parlamentarians
from .serializers import ParlamentariansSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
import requests, json

@api_view(['GET'])
@parser_classes((JSONParser,))

def parlamentarians(request, format=None):
    parlamentarians = Parlamentarians.objects.all()

    if parlamentarians:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    else:
        serializer = ParlamentariansSerializer(parlamentarians)
        r = requests.get('Parlamentarians',serializer)
        data = json.loads(r.text)

        return Response(data, status=status.HTTP_201_CREATED)
