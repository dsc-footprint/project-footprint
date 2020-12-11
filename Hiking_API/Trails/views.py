from django.shortcuts import get_object_or_404, render
from .models import Trail
from Users.models import UserStats
from .serializers import (UserCompletedTrailsSerializer)
from rest_framework import viewsets, permissions, generics
from rest_framework.views import APIView 
from rest_framework.viewsets import ModelViewSet
from django.contrib.sites import requests
from rest_framework.response import Response
from rest_framework.utils import json

# class based view, inherit from ModelViewSet
class UserCompletedTrailsListView(viewsets.ModelViewSet):
    queryset = Trail.objects.all()
    serializer_class = UserCompletedTrailsSerializer
    permission_classes = [permissions.IsAuthenticated]

class Trails(viewsets.ModelViewSet):
    queryset = Trail.objects.all()
    serializer_class = UserCompletedTrailsSerializer
    permission_classes = [permissions.IsAuthenticated]
    fields = ['lat', 'long']

    def call_api(self, request, *args, **kwargs):
        import os
        API_KEY = os.getenv("API_KEY")
        headers = {}
        url = 'https://www.hikingproject.com/data/get-trails?lat=' + lat + '&lon=' + long + '&maxDistance=10&key=' + API_KEY
        method = request.method.lower()
        method_map = {
            'get': requests.get,
            'post': requests.post,
            'put': requests.put,
            'patch': requests.patch,
            'delete': requests.delete
        }
        return Response(method_map[method](url, headers=headers, data=json.dumps(request.data)).json())

    def get(self, request, *args, **kwargs):
        return self.call_api(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.call_api(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.call_api(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.call_api(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.call_api(request, *args, **kwargs)