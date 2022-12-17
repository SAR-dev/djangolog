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
        
class CommentFilter(filters.FilterSet):
    o = filters.OrderingFilter(
        fields=(
            ('created_at', 'created_at'),
        ),
    )
    class Meta:
        model = Comment
        fields = {
            'gig__id': ['exact']
        }

class CommentCreateView(generics.CreateAPIView):
    def perform_create(self, serializer):
        rated = False
        if self.request.data["rating"]:  # type: ignore
            rated = Comment.ratings.filter(gig_id=self.request.data['gig']).exists()  # type: ignore
        if(rated == True):
            raise NotFound(detail="Error 404, You have already rated this gig!", code=404)
        else:
            serializer.save(author=self.request.user)

    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentWriteSerializer
    pagination_class = PazeSizePagination
    filterset_class = CommentFilter

class CommentListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentReadSerializer
    pagination_class = PazeSizePagination
    filterset_class = CommentFilter

class CommentRetriveView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentReadSerializer

class CommentUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCommentAuthor]
    queryset = Comment.objects.all()
    serializer_class = CommentWriteSerializer

