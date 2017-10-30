import requests, json
from django.shortcuts import render
from .models import Parlamentarians
from rest_framework.decorators import api_view
from .serializers import ParlamentariansSerializer
from django.http import HttpResponse, JsonResponse
import json

@api_view(['GET'])
def parlamentarians(request):
        parlamentarians = Parlamentarians.objects.all()
        parlamentary = (Parlamentarians.objects.all()[:1].get())
        print(parlamentary.parlamentaryPhotoPath)
        serializer = ParlamentariansSerializer(parlamentarians, many=True)
        return JsonResponse(serializer.data, safe=False)
