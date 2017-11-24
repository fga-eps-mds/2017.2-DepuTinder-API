from rest_framework import serializers
from .models import Questionnaire

class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ('maxQuestions', 'totalQuestions')
