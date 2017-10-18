from django.db import models

class Parlamentarians(models.Model):

    parlamentaryPhotoPath = models.CharField(max_length=500, blank=False, default="https://i.imgur.com/ylkRU02.png")
    parlamentaryName = models.CharField(max_length=150, blank=False)
    parlamentaryUF = models.CharField(max_length=3, blank=False)
    parlamentaryPoliticalParty = models.CharField(max_length=6, blank=False)
