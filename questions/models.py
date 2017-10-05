from django.db import models


class Questions(models.Model):
    # Vote will be caught as an int, and will be interpreted on the front-end
    # -1 = NAO / 0 = ME ABSTENHO / 1 = SIM
    questionAnswer = models.IntegerField(blank=False)