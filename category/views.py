from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer, CategoryFeedSerializer
from utils.paginations import PazeSizePagination
from rest_framework import generics, views, response, permissions, exceptions, status

class CategoryListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = PazeSizePagination

class CategoryFeedListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategoryFeedSerializer
    queryset = Category.objects.all()
    pagination_class = PazeSizePagination

class CategoryFeedRtriveView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategoryFeedSerializer
    queryset = Category.objects.all()