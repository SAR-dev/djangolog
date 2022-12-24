from django.shortcuts import render
from .models import Comment
from .serializers import CommentReadSerializer, CommentWriteSerializer
from rest_framework import generics, views, response, permissions, exceptions, status
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist
from django_filters import rest_framework as filters
from utils.paginations import PazeSizePagination

class IsCommentAuthor(permissions.BasePermission):
    message = 'You can not view this route!'

    def has_permission(self, request, view):
        try:
            comment = Comment.objects.get(pk=view.kwargs.get('pk'))
            author = comment.author == request.user
            return author
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)

class CommentCreateView(generics.CreateAPIView):
    def perform_create(self, serializer):
        rated = False
        if self.request.data["rating"]:  # type: ignore
            rated = Comment.ratings.filter(comment_id=self.request.data['comment']).exists()  # type: ignore
        if(rated == True):
            raise NotFound(detail="Error 404, You have already rated this comment!", code=404)
        else:
            serializer.save(author=self.request.user)

    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentWriteSerializer
    pagination_class = PazeSizePagination

class CommentListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentReadSerializer
    pagination_class = PazeSizePagination

class CommentRetriveView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentReadSerializer

class CommentUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    def perform_create(self, serializer):
        rated = False
        if self.request.data["rating"]:  # type: ignore
            rated = Comment.ratings.filter(comment_id=self.request.data['comment']).exists()  # type: ignore
        if(rated == True):
            raise NotFound(detail="Error 404, You have already rated this comment!", code=404)
        else:
            serializer.save()

    permission_classes = [IsCommentAuthor]
    queryset = Comment.objects.all()
    serializer_class = CommentWriteSerializer

class CommentUpVoteView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            if request.user not in comment.upvotes.all():
                comment.upvotes.add(request.user)
                comment.downvotes.remove(request.user)
            return response.Response(
                {
                    "num_vote_up": comment.upvotes.count(),
                    "num_vote_down": comment.downvotes.count(),
                }
            )
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)
        
    def delete(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            if request.user in comment.upvotes.all():
                comment.upvotes.remove(request.user)
            return response.Response(
                {
                    "num_vote_up": comment.upvotes.count(),
                    "num_vote_down": comment.downvotes.count(),
                }
            )
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)

class CommentDownVoteView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            if request.user not in comment.downvotes.all():
                comment.downvotes.add(request.user)
                comment.upvotes.remove(request.user)
            return response.Response(
                {
                    "num_vote_up": comment.upvotes.count(),
                    "num_vote_down": comment.downvotes.count(),
                }
            )
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)
        
    def delete(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            if request.user in comment.downvotes.all():
                comment.downvotes.remove(request.user)
            return response.Response(
                {
                    "num_vote_up": comment.upvotes.count(),
                    "num_vote_down": comment.downvotes.count(),
                }
            )
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)
        