from django.db import models
from question.models import Question

class Questionnaire(models.Model):
    maxQuestions = models.IntegerField(blank=False, default=10)
    totalQuestions = models.IntegerField(blank=False, )
