from django.db import models

class Parlamentarians(models.Model):
    candidadeName = models.CharField(max_length=150, blanck=False)
    candidateDescription = models.CharField(max_length=500, blanck=True)

# In the future will be add two more atributes: State Foreing key and PoliticalParty Foreign key.
