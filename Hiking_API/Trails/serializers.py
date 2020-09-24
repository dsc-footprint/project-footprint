from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Trail
from django.contrib.auth.models import Permission


class UserCompletedTrailsSerializer(ModelSerializer):
    class Meta:
        model = Trail
        fields = ['ID', 'UserCompleted']
