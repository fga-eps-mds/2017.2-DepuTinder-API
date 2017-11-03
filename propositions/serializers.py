from rest_framework import serializers
from .models import Propositions

class PropositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propositions
        fields = ('id','propositionTitle', 'propositionSubTitle', 'propositionDescription', 'propositionAuthor', 'propositionLink')
