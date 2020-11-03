from django.shortcuts import get_object_or_404, render
from .models import UserStats
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, permissions, generics
from .serializers import (UserStatsSerializer)

# Create your views here.


# class based view, inherit from ModelViewSet
class UserStatsListView(viewsets.ModelViewSet):
    queryset = UserStats.objects.all()
    serializer_class = UserStatsSerializer
    permission_classes = [permissions.IsAuthenticated]

