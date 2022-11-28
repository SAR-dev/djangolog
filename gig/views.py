from django.shortcuts import render
from gig.models import Gig
from gig.serializers import GigSerializer
from rest_framework import generics, views, response, permissions, exceptions, status
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist

class IsGigAuthor(permissions.BasePermission):
    message = 'You can not view this route!'

    def has_permission(self, request, view):
        try:
            gig = Gig.objects.get(pk=view.kwargs.get('pk'))
            author = gig.author == request.user
            return author
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)

class GigCategoryListCreateView(generics.ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    permission_classes = [permissions.IsAuthenticated]
    queryset = Gig.objects.all()
    serializer_class = GigSerializer

class GigRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Gig.objects.all()
    serializer_class = GigSerializer

