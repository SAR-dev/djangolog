from django.shortcuts import render
from .models import Gig
from .serializers import GigWriteSerializer, GigReadSerializer
from rest_framework import generics, views, response, permissions, exceptions, status
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist
from django_filters import rest_framework as filters
from utils.paginations import PazeSizePagination

class IsGigAuthor(permissions.BasePermission):
    message = 'You can not view this route!'

    def has_permission(self, request, view):
        try:
            gig = Gig.objects.get(pk=view.kwargs.get('pk'))
            author = gig.author == request.user
            return author
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)
        
class GigFilter(filters.FilterSet):
    o = filters.OrderingFilter(
        fields=(
            ('title', 'title'),
            ('created_at', 'created_at'),
        ),
    )
    class Meta:
        model = Gig
        fields = {
            'title': ['icontains'],
            'description': ['icontains'],
            'category__slug': ['exact']
        }

class GigCreateView(generics.ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    permission_classes = [permissions.IsAuthenticated]
    queryset = Gig.objects.all()
    serializer_class = GigWriteSerializer
    pagination_class = PazeSizePagination
    filterset_class = GigFilter

class GigListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Gig.objects.all()
    serializer_class = GigReadSerializer
    pagination_class = PazeSizePagination
    filterset_class = GigFilter

class GigRetriveView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Gig.objects.all()
    serializer_class = GigReadSerializer

class GigUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsGigAuthor]
    queryset = Gig.objects.all()
    serializer_class = GigWriteSerializer

