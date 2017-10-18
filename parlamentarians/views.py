import requests, json
from django.shortcuts import render
from .models import Parlamentarians
from rest_framework.decorators import api_view
from django.core import serializers
from django.http import HttpResponse
@api_view(['GET'])
def parlamentarians(request, format=json):
    parlamentarians = Parlamentarians.objects.all()
    if parlamentarians:
        data = serializers.serialize('json', parlamentarians)
        return HttpResponse(data, content_type='application/json')
