from django.db import models

NAME_LENGTH = 150
EMAIL_LENGTH = 150
PASSWORD_LENGTH = 150
IMAGE_LENGTH = 150

class Users(models.Model):
	userName = models.CharFiled(max_length = NAME_LENGTH, blank = False)
	userEmail = models.CharFiled(max_length = EMAIL_LENGTH, blank = False)
	userPassword = models.CharFiled(max_length = PASSWORD_LENGTH, blank = False)
	userImage = models.TextFiled(max_length = IMAGE_LENGTH, blank = True)

