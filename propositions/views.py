from django.shortcuts import render
from .models import Propositions
from .serializers import PropositionsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def propositions(request):
    propositions = Propositions.objects.all()

    if propositions:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    else:
        serializer = PropositionsSerializer(propositions)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
