from django.db import models
from question.models import Question

class Questionnaire(models.Model):

    questionsFK = models.ManyToManyField(Question)

    def __str__(self):
        return self.questionsFK
