from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    listingCategory = models.CharField(max_length=100)

    def __str__(self):
        return self.listingCategory
    
class listings(models.Model):
    '''
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=3000)
    active = models.BooleanField(default=True)
    price = models.FloatField()
    image = models.CharField(max_length=3000)
    listingCategory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")


