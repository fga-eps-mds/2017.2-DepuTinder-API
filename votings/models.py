from django.db import models
class Votings(models.Model):
    # Vote will be caught as an int, and will be interpreted on the front-end
    # -1 = NAO / 0 = ME ABSTENHO / 1 = SIM

    propositionID = models.ForeignKey(
        'propositions.Propositions',
        on_delete = models.CASCADE,
        related_name = '%(class)s_id',
        default=0,
        null=True)

    candidateID = models.ForeignKey(
        'parlamentarians.Parlamentarians',
        on_delete = models.CASCADE,
        related_name = 'candidateID',
        default=0,
        null=True)

    candidateVote = models.IntegerField(blank=False)
