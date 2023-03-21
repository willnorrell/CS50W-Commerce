from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class listings(models.Model):
    '''
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
    '''
    owner = User
    