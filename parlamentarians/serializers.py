from rest_framework import serializers
from .models import Parlamentarians

class ParlamentariansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parlamentarians
        fields = ('parlamentaryPhotoPath', 'parlamentaryName', 'parlamentaryUF', 'parlamentaryPoliticalParty')
