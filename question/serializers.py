from rest_framework import serializers
from .models import Question
from propositions.serializers import PropositionsSerializer

class QuestionSerializer(serializers.Serializer):
    questionTitle = serializers.CharField()
    questionSubtitle = serializers.CharField()
    questionDescription = serializers.CharField()
    questionAuthor = serializers.CharField()
    propositionFK = serializers.ReadOnlyField()

    class Meta:
        model = Question
        fields = (
            'questionTitle',
            'questionSubtitle',
            'questionDescription',
            'questionAuthor',
            'propositionFK',)
