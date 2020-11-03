from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .serializers import (FavouriteTrailsSerializer)
from .models import FavouriteTrails

# Create your views here.
class FavouriteTrailsView(viewsets.ModelViewSet):
    queryset = FavouriteTrails.objects.all()
    serializer_class = FavouriteTrailsSerializer
    permission_classes = [permissions.IsAuthenticated]