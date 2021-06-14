from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	handle=models.CharField(max_length=20)
	biograph=models.TextField(max_length=200)