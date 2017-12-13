from django.db import models

# Create your models here.

TITLE_LENGTH = 100
SUBTITLE_LENGTH = 150
DESCRIPTION_LENGTH = 200
AUTHOR_LENGTH = 50

class Question(models.Model):
    proposition = models.ForeignKey(
        'propositions.Propositions',
        on_delete=models.CASCADE,
        related_name='proposition',
    )
    questionnaire = models.ForeignKey(
        'questionnaire.Questionnaire',
        on_delete=models.CASCADE,
        related_name='questionnaire',
    )
    questionTitle = models.CharField(max_length=TITLE_LENGTH, blank=True)
    questionSubtitle = models.CharField(max_length=SUBTITLE_LENGTH, blank=True)
    questionDescription = models.CharField(max_length=DESCRIPTION_LENGTH, blank=True)
    questionAuthor = models.CharField(max_length=AUTHOR_LENGTH, blank=True)

    @property
    def propositionFK(self):
        return self.proposition.id

    @property
    def questionnaireFK(self):
        return self.questionnaire.id
