from django.db import models
from django.contrib.auth.models import User

IMAGE_LENGTH = 5000

class Users(models.Model):
    user = models.OneToOneField(User)
    userImage = models.TextField(max_length = IMAGE_LENGTH, blank = True)
