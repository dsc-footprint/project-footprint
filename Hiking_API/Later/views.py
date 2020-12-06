from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .serializers import (LaterTrailsSerializer)
from .models import LaterTrails

class LaterTrailsView(viewsets.ModelViewSet):
    queryset = LaterTrails.objects.all()
    serializer_class = LaterTrailsSerializer
    permission_classes = [permissions.IsAuthenticated]
