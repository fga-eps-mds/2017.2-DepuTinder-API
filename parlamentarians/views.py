from django.shortcuts import render
from .models import Parlamentarians
from .serializers import ParlamentariansSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests, json

@api_view(['GET'])
def parlamentarians(request):
    