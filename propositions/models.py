from django.db import models

class Propositions(models.Model):
    propositionTitle = models.CharField(max_length=100, blank=True)
    propositionSubTitle = models.CharField(max_length=150, blank=True)
    propositionDescription = models.CharField(max_length=200, blank=True)
    propositionAuthor = models.CharField(max_length=50, blank=True)
