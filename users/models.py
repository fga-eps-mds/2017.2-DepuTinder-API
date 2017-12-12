from django.db import models
from django.contrib.auth.models import User

LENGTH = 5000

class Users(models.Model):
    user = models.ForeignKey(User, related_name='User', null=True)
    userImage = models.TextField(max_length = LENGTH, blank = True)
    userToken = models.TextField(max_length = LENGTH, blank = True)
