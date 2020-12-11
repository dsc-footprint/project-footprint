from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework import generics, permissions, status, viewsets
from .serializers import (LaterTrailsSerializer)
from .models import LaterTrails
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from django.http.response import Http404

class LaterTrailsView(viewsets.ModelViewSet):
    queryset = LaterTrails.objects.all()
    serializer_class = LaterTrailsSerializer
    permission_classes = [permissions.IsAuthenticated]

#delete
class LaterTrailsDeleteView(DestroyAPIView):
    queryset = LaterTrails.objects.all()
    serializer_class = LaterTrailsSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'user_id', 'trail_id'