from django.db import models

class Questionnaire(models.Model):
    questionnaireID = models.PositiveIntegerField(blank=False)
