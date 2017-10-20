from rest_framework import serializers
from .models import Answers

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ('user', 'proposition', 'answerType')
