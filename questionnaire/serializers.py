from rest_framework import serializers
from .models import Questionnaire
from question.serializers import QuestionSerializer

class QuestionnaireSerializer(serializers.ModelSerializer):
    questionsFK = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='id',
        default=0)

    class Meta:
        model = Questionnaire
        fields = ('questionsFK')
