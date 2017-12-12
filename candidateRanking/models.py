from django.db import models

class CandidateRanking(models.Model):
    ranking = models.CharField(max_length=5000)
