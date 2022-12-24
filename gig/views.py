from django.shortcuts import render
from .models import Gig
from .serializers import GigWriteSerializer, GigReadSerializer
from rest_framework import generics, views, response, permissions, exceptions, status
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist
from django_filters import rest_framework as filters
from utils.paginations import PazeSizePagination
from django.db.models import Q

class IsGigAuthor(permissions.BasePermission):
    message = "You can not view this route!"

    def has_permission(self, request, view):
        try:
            gig = Gig.objects.get(pk=view.kwargs.get("pk"))
            author = gig.author == request.user
            return author
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)

class CheckIfGigMaxed(permissions.BasePermission):
    message = "You already have maximum amount (10) of gigs!"

    def has_permission(self, request, view):
        try:
            gigs = Gig.objects.filter(author__username=request.user.username)
            return gigs.count() <= 10
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)


class GigFilter(filters.FilterSet):
    o = filters.OrderingFilter(
        fields=(
            ("title", "title"),
            ("created_at", "created_at"),
        ),
    )

    class Meta:
        model = Gig
        fields = {
            "title": ["icontains"],
            "description": ["icontains"],
            "category__slug": ["exact"],
            "author__id": ["exact"],
            "author__username": ["exact"]
        }


class GigCreateView(generics.CreateAPIView):
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    permission_classes = [CheckIfGigMaxed]
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

class GigSearchView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GigReadSerializer
    pagination_class = PazeSizePagination

    def get_queryset(self):
        keyword = self.kwargs["keyword"]
        if (len(keyword) < 3):
            raise NotFound(detail="Search keyword too short", code=404)
        else:
            return Gig.objects.filter(Q(tags__contains=[keyword]) | Q(title__contains=keyword))


class GigRetriveView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Gig.objects.all()
    serializer_class = GigReadSerializer


class GigUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsGigAuthor]
    queryset = Gig.objects.all()
    serializer_class = GigWriteSerializer


class GigUpVoteView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            gig = Gig.objects.get(pk=pk)
            if request.user not in gig.upvotes.all():
                gig.upvotes.add(request.user)
                gig.downvotes.remove(request.user)
            return response.Response(
                {
                    "num_vote_up": gig.upvotes.count(),
                    "num_vote_down": gig.downvotes.count(),
                }
            )
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)
        
    def delete(self, request, pk):
        try:
            gig = Gig.objects.get(pk=pk)
            if request.user in gig.upvotes.all():
                gig.upvotes.remove(request.user)
            return response.Response(
                {
                    "num_vote_up": gig.upvotes.count(),
                    "num_vote_down": gig.downvotes.count(),
                }
            )
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)

class GigDownVoteView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            gig = Gig.objects.get(pk=pk)
            if request.user not in gig.downvotes.all():
                gig.downvotes.add(request.user)
                gig.upvotes.remove(request.user)
            return response.Response(
                {
                    "num_vote_up": gig.upvotes.count(),
                    "num_vote_down": gig.downvotes.count(),
                }
            )
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)
        
    def delete(self, request, pk):
        try:
            gig = Gig.objects.get(pk=pk)
            if request.user in gig.downvotes.all():
                gig.downvotes.remove(request.user)
            return response.Response(
                {
                    "num_vote_up": gig.upvotes.count(),
                    "num_vote_down": gig.downvotes.count(),
                }
            )
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)
        
class GigUpvotedListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GigReadSerializer
    pagination_class = PazeSizePagination
    filterset_class = GigFilter

    def get_queryset(self):
        return Gig.objects.filter(upvotes__id=self.request.user.id)