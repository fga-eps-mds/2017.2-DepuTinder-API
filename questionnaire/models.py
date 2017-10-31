from django.db import models

class Questionnaire(models.Model):
    questionnaireID = models.PositiveIntegerField(blank=False, primary_key=True)
    questionsTotal = models.PositiveIntegerField(blank=False, default=10)
