from django.shortcuts import render
from rest_framework import generics, views, response, permissions, exceptions, status
from .models import Advertisement
from .serializers import AdvertisementSerializer

class AdvertisementListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer