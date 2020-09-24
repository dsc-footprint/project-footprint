from django.db import models
from Users.models import UserStats


# Create your models here.
class Trail(models.Model):
    ID = models.CharField(max_length=100)
    UserCompleted = models.ManyToManyField(UserStats, blank=True)
