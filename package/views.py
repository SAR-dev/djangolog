from django.shortcuts import render
from .models import Package
from .serializers import PackageReadSerializer, PackageWriteSerializer
from rest_framework import generics, views, response, permissions, exceptions, status
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist
from django_filters import rest_framework as filters
from utils.paginations import PazeSizePagination

class IsPackageAuthor(permissions.BasePermission):
    message = 'You can not view this route!'

    def has_permission(self, request, view):
        try:
            package = Package.objects.get(pk=view.kwargs.get('pk'))
            author = package.author == request.user
            return author
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)
        
class PackageFilter(filters.FilterSet):
    o = filters.OrderingFilter(
        fields=(
            ('title', 'title'),
            ('created_at', 'created_at'),
        ),
    )
    class Meta:
        model = Package
        fields = {
            'title': ['icontains'],
            'description': ['icontains'],
            'gig__id': ['exact']
        }

class PackageCreateView(generics.ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    permission_classes = [permissions.IsAuthenticated]
    queryset = Package.objects.all()
    serializer_class = PackageWriteSerializer
    pagination_class = PazeSizePagination
    filterset_class = PackageFilter

class PackageListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Package.objects.all()
    serializer_class = PackageReadSerializer
    pagination_class = PazeSizePagination
    filterset_class = PackageFilter

class PackageRetriveView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Package.objects.all()
    serializer_class = PackageReadSerializer

class PackageUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsPackageAuthor]
    queryset = Package.objects.all()
    serializer_class = PackageWriteSerializer

