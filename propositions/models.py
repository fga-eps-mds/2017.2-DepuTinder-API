from django.db import models

TITLE_LENGTH = 100
SUBTITLE_LENGTH = 150
DESCRIPTION_LENGTH = 200
AUTHOR_LENGTH = 50
LINK_LENGTH = 5000

class Propositions(models.Model):
    questionnaire = models.ForeignKey(
        'questionnaire.Questionnaire',
        on_delete=models.CASCADE,
        related_name='propositionID',
        default=0)
    propositionTitle = models.CharField(max_length=TITLE_LENGTH, blank=True)
    propositionSubTitle = models.CharField(max_length=SUBTITLE_LENGTH, blank=True)
    propositionDescription = models.CharField(max_length=DESCRIPTION_LENGTH, blank=True)
    propositionAuthor = models.CharField(max_length=AUTHOR_LENGTH, blank=True)
    propositionLink = models.CharField(max_length=LINK_LENGTH, blank=True)
