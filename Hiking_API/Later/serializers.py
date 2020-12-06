
from .models import LaterTrails
from rest_framework import serializers

class LaterTrailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaterTrails
        fields = ('trail_id', 'user_id')