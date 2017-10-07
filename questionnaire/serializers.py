from rest_framework import serializers
from .models import Questionnaire

class QuestionnaireSerializer(serializers.ModelSerializer):
    propositionID = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='id',
        default=0)

    questions = serializers.ListField(propositionID)

    class Meta:
        model = Questionnaire
        fields = ('questions')
