from django.db import models

class CandidateRanking(models.Model):
    ranking = models.CharField(max_length=999999)
