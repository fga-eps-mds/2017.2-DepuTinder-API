from rest_framework import serializers
from .models import Votings
from propositions.serializers import PropositionsSerializer
from parlamentarians.serializers import ParlamentariansSerializer

class VotingsSerializer (serializers.Serializer):
    propositionID = PropositionsSerializer(many=False)
    candidateID = ParlamentariansSerializer(many=False)
    class Meta:
        model = Votings
        fields = ('propositionID', 'candidateID', 'candidateVote')
