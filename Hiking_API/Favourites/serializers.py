
from .models import FavouriteTrails
from rest_framework import serializers

class FavouriteTrailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteTrails
        fields = '__all__'