from rest_framework import serializers
from .models import Questions

class QuestionsSerializer (serializers.Serializer):
    class Meta:
        model = Questions
        fields = ('QuestionId', 'QuestionAnswer')
