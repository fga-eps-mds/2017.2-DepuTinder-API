from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET'])

# request parameter must be here
def rankingIndex(request):
    rankingResultData = {
     "data": [
        {"groupID":90,"candidates":["Armando"]},
        {"groupID":80,"candidates":["Donelle","Sammy","Thor"]},
        {"groupID":70,"candidates":["Loise","Burtie"]},
        {"groupID":60,"candidates":["Alejandrina","Cleveland","Ronda"]}
     ],
    }
    return Response(rankingResultData, status=status.HTTP_200_OK)
