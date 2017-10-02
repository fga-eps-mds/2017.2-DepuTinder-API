from django.db import models

NAME_LENGTH = 100
class Ranking(models.Model):
    groupID = models.IntegerField(blank=False)
    candidatesNames = models.CharField(max_length=NAME_LENGTH)
