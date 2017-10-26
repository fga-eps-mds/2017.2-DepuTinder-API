from django.db import models
class Votings(models.Model):
    # Vote will be caught as an int, and will be interpreted on the front-end
    # -1 = NAO / 0 = ME ABSTENHO / 1 = SIM

    propositionID = models.ForeignKey(
        'propositions.Propositions',
        on_delete = models.CASCADE,
        related_name = 'propositionID',
        default=0)

    candidateID = models.ForeignKey(
        'parlamentarians.Parlamentarians',
        on_delete = models.CASCADE,
        related_name = 'candidateID',
        default=0)

    candidateVote = models.IntegerField(blank=False)
