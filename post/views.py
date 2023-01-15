from django.shortcuts import render
from .models import Post
from .serializers import PostReadSerializer, PostWriteSerializer
from rest_framework import generics, views, response, permissions, exceptions, status
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist
from django_filters import rest_framework as filters
from utils.paginations import PazeSizePagination

class IsPostAuthor(permissions.BasePermission):
    message = 'You can not view this route!'

    def has_permission(self, request, view):
        try:
            post = Post.objects.get(pk=view.kwargs.get('pk'))
            author = post.author == request.user
            return author
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)

class PostCreateView(generics.CreateAPIView):
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostWriteSerializer
    pagination_class = PazeSizePagination

class PostListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostReadSerializer
    pagination_class = PazeSizePagination

class PostRetriveView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostReadSerializer

class PostUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsPostAuthor]
    queryset = Post.objects.all()
    serializer_class = PostWriteSerializer

class PostUpVoteView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            if request.user not in post.upvotes.all():
                post.upvotes.add(request.user)
                post.downvotes.remove(request.user)
            return response.Response(
                {
                    "num_vote_up": post.upvotes.count(),
                    "num_vote_down": post.downvotes.count(),
                }
            )
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)
        
    def delete(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            if request.user in post.upvotes.all():
                post.upvotes.remove(request.user)
            return response.Response(
                {
                    "num_vote_up": post.upvotes.count(),
                    "num_vote_down": post.downvotes.count(),
                }
            )
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)

class PostDownVoteView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            if request.user not in post.downvotes.all():
                post.downvotes.add(request.user)
                post.upvotes.remove(request.user)
            return response.Response(
                {
                    "num_vote_up": post.upvotes.count(),
                    "num_vote_down": post.downvotes.count(),
                }
            )
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)
        
    def delete(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            if request.user in post.downvotes.all():
                post.downvotes.remove(request.user)
            return response.Response(
                {
                    "num_vote_up": post.upvotes.count(),
                    "num_vote_down": post.downvotes.count(),
                }
            )
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)
        