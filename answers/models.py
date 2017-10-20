from django.db import models
from users.models import Users
from propositions.models import Propositions

class Answers(models.Model):
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='userID')
    proposition = models.ForeignKey(
        Propositions,
        on_delete=models.CASCADE,
        related_name='propositionID')
    answerType = models.CharField(null=True, blank=True, max_length=100) # 1-SIM / 2-NAO / 3-ABSTENHO
