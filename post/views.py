from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from utils.paginations import PazeSizePagination

class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.published.all()
    pagination_class = PazeSizePagination

class PostRetriveView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.published.all()