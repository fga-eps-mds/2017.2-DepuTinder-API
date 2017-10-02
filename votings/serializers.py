from rest_framework import serializers
from .models import Votings

class VotingsSerializer (serializers.Serializer):
    class Meta:
        model = Votings
        fields = ('CandidateId', 'CandidateVote')
