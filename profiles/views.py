from django.shortcuts import render
from .models import Profiles
from .serializers import ProfilesWriteSerializer, ProfilesReadSerializer
from rest_framework import generics, views, response, permissions, exceptions, status
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist
from django_filters import rest_framework as filters
from utils.paginations import PazeSizePagination


class IsProfilesAuthor(permissions.BasePermission):
    message = "You can not view this route!"

    def has_permission(self, request, view):
        try:
            profile = Profiles.objects.get(pk=view.kwargs.get("pk"))
            author = profile.author == request.user
            return author
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)


class ProfilesFilter(filters.FilterSet):
    o = filters.OrderingFilter(
        fields=(
            ("created_at", "created_at"),
        ),
    )

    class Meta:
        model = Profiles
        fields = {
            "author__id": ["exact"],
            "author__username": ["exact"]
        }


class ProfilesCreateView(generics.CreateAPIView):
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    permission_classes = [permissions.IsAuthenticated]
    queryset = Profiles.objects.all()
    serializer_class = ProfilesWriteSerializer
    pagination_class = PazeSizePagination
    filterset_class = ProfilesFilter


class ProfilesListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profiles.objects.all()
    serializer_class = ProfilesReadSerializer
    pagination_class = PazeSizePagination
    filterset_class = ProfilesFilter


class ProfilesRetrieveView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfilesReadSerializer

    def get_object(self):
        try:
            return Profiles.objects.get(author__id=self.request.user.id)
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)

class ProfilesRetrieveByUsernameView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfilesReadSerializer

    def get_object(self):
        try:
            return Profiles.objects.get(author__username=self.kwargs['username'])
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)

class ProfilesUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfilesWriteSerializer

    def get_object(self):
        try:
            return Profiles.objects.get(author__id=self.request.user.id)
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)
