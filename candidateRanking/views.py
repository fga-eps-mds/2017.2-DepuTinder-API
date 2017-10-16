from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RankingSerializer
from rest_framework.decorators import detail_route
from .models import Ranking
from rest_framework.response import Response

class RankingViewSet(viewsets.ModelViewSet):
    serializer_class = RankingSerializer

    @detail_route(methods=['GET'])
    def listRanking(self, request, userID):
        userID = request.query_params['userID']
        //tratar
        ranking = Ranking.objects.get(userID = userID)
        serializer_ranking = RankingSerializer(ranking, many=False).data
        return Response(serializer_ranking)
