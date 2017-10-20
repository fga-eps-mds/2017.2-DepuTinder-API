from rest_framework import serializers
from .models import Answers

class AnswersSerializer(serializers.Serializer):
    class Meta:
        model = Answers
        fields = ('userFK', 'propositionFK', 'ansewrType')
