from rest_framework import serializers
from .models import *

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('candidateName', 'candidateDescripition', 'partyCandidate')

class CandidateListSerializer(serializers.ModelSerializer):
    candidate = CandidateSerializer(many=True)
    class Meta:
        model = CandidateList
        fields = ('candidate')

class CandidateGroupSerializer(serializers.ModelSerializer):
    candidateList = CandidateListSerializer(many=False)
    class Meta:
        model = CandidateGroupSerializer
        fields = ('groupPercentage', 'candidateList')

class UserIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserID
        fields = ('userID')

class RankingSerializer(serializers.ModelSerializer):
    userID = UserIDSerializer(many=False)
    candidateGroup = CandidateGroupSerializer(many=True)
    class Meta:
        model = Ranking
        fields = ('userID', 'candidateGroup')
