from django.db import models

class Votings(models.Model):
    CandidateId = models.PositiveIntegerField(blank=False)

    # Vote will be caught as an int.
    # -1 = NAO / 0 = ME ABSTENHO / 1 = SIM
    CandidateVote = models.IntegerField(blank=False)
