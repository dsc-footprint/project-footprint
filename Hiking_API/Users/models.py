from django.db import models
from Hiking_API.Trails.models import Trail as trails

# Create your models here.
class UserStats(models.Model):
    UID = models.CharField(max_length=100)
    completedTrails = models.ManyToManyField(trails, blank=True)