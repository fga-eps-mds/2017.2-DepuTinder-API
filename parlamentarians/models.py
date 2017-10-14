from django.db import models

class Parlamentarians(models.Model):
    parlamentaryName = models.CharField(max_length=150, blank=False)
    parlamentaryUF = models.CharField(max_length=3, blank=False)
    parlamentaryPoliticalParty = models.IntegerField(blank=False)
