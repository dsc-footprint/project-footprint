from django.db import models

class FavouriteTrails(models.Model):
    trail_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
