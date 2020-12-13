from rest_framework import viewsets
from . import models
from . import serializers

class FavouritesViewSets(viewsets.ModelViewSet):
    queryset = models.FavouriteTrails.objects.all()
    serializer_class = serializers.FavouriteTrailsSerializer