from django.shortcuts import get_object_or_404, render
from .models import Trail
from Users.models import UserStats
from .serializers import (UserCompletedTrailsSerializer)
from rest_framework import viewsets, permissions, generics

from rest_framework.viewsets import ModelViewSet

# class based view, inherit from ModelViewSet
class UserCompletedTrailsListView(viewsets.ModelViewSet):
    queryset = Trail.objects.all()
    serializer_class = UserCompletedTrailsSerializer
    permission_classes = [permissions.IsAuthenticated]