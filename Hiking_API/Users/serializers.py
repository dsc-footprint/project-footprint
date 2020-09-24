from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import UserStats
from django.contrib.auth.models import Permission


class UserStatsSerializer(ModelSerializer):
    class Meta:
        model = UserStats
        fields = ['UID']
