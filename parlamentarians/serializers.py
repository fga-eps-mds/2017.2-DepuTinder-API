from rest_framework import serializers
from .models import Parlamentarians

class ParlamentariansSerializer(serializers.Serializer):
    class Meta:
        model = Parlamentarians
        fields = ('parlamentaryName', 'parlamentaryUF', 'parlamentaryPoliticalParty')
