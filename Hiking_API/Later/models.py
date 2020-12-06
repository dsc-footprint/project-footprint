from django.db import models

# Create your models here.
class LaterTrails(models.Model):
    trail_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
