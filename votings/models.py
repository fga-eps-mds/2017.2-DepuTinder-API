from django.db import models

class Votings(models.Model):
    candidateId = models.PositiveIntegerField(blank=False)

    # Vote will be caught as an int, and will be interpreted on the front-end
    # -1 = NAO / 0 = ME ABSTENHO / 1 = SIM
    candidateVote = models.IntegerField(blank=False)
