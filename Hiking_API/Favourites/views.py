from django.shortcuts import render
from rest_framework import generics, permissions, status, viewsets
from .serializers import (FavouriteTrailsSerializer)
from .models import FavouriteTrails
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
class FavouriteTrailsView(viewsets.ModelViewSet):
    queryset = FavouriteTrails.objects.all()
    serializer_class = FavouriteTrailsSerializer
    permission_classes = [permissions.IsAuthenticated]

'''@api_view(['PUT', 'DELETE'])
def put_and_delete(request, pk):

    try:
        f_trails = FavouriteTrails.objects.get(pk=pk)
    except FavouriteTrails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        queryset = FavouriteTrails.objects.all()
        serializer = FavouriteTrailsSerializer(f_trails, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        f_trails.delete() '''
