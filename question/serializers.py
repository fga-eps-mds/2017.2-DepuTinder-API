from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.Serializer):
    propositionFK = serializers.RelatedField(source='proposition', read_only=True)
    questionnaireFK = serializers.RelatedField(source='questionnaire', read_only=True)

    class Meta:
        model = Question
        fields = (
            'questionTitle',
            'questionSubtitle',
            'questionDescription',
            'questionAuthor',
            'propositionFK',
            'questionnaireFK')
