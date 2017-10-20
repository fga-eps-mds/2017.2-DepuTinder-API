from django.db import models

class Answers(models.Model):
    users = models.ForeignKey(
        'users.Users',
        on_delete=models.CASCADE,
        related_name='userFK')
    propositions = models.ForeignKey(
        'propositions.Propositions',
        on_delete=models.CASCADE,
        related_name='propositionFK')
    ansewrType = models.IntegerField() # 1-SIM / 2-NAO / 3-ABSTENHO

