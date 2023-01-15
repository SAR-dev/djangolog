from django.shortcuts import render
from .models import Event
from .serializers import EventWriteSerializer, EventReadSerializer
from rest_framework import generics, views, response, permissions, exceptions, status
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist
from django_filters import rest_framework as filters
from utils.paginations import PazeSizePagination
from django.db.models import Q

class IsEventAuthor(permissions.BasePermission):
    message = "You can not view this route!"

    def has_permission(self, request, view):
        try:
            event = Event.objects.get(pk=view.kwargs.get("pk"))
            author = event.author == request.user
            return author
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)

class CheckIfEventMaxed(permissions.BasePermission):
    message = "You already have maximum amount (10) of events!"

    def has_permission(self, request, view):
        try:
            events = Event.objects.filter(author__username=request.user.username)
            return events.count() <= 10
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)


class EventFilter(filters.FilterSet):
    o = filters.OrderingFilter(
        fields=(
            ("title", "title"),
            ("created_at", "created_at"),
        ),
    )

    class Meta:
        model = Event
        fields = {
            "name": ["icontains"],
            "description": ["icontains"],
            "category__slug": ["exact"],
            "author__id": ["exact"],
            "author__username": ["exact"]
        }


class EventCreateView(generics.CreateAPIView):
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    permission_classes = [CheckIfEventMaxed]
    queryset = Event.objects.all()
    serializer_class = EventWriteSerializer
    pagination_class = PazeSizePagination
    filterset_class = EventFilter


class EventListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventReadSerializer
    pagination_class = PazeSizePagination
    filterset_class = EventFilter

class EventSearchView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EventReadSerializer
    pagination_class = PazeSizePagination

    def get_queryset(self):
        keyword = self.kwargs["keyword"]
        if (len(keyword) < 3):
            raise NotFound(detail="Search keyword too short", code=404)
        else:
            return Event.objects.filter(Q(tags__contains=[keyword]) | Q(title__contains=keyword))

class EventRetriveView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventReadSerializer


class EventUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsEventAuthor]
    queryset = Event.objects.all()
    serializer_class = EventWriteSerializer


class EventUpVoteView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            if request.user not in event.upvotes.all():
                event.upvotes.add(request.user)
                event.downvotes.remove(request.user)
            return response.Response(
                {
                    "num_vote_up": event.upvotes.count(),
                    "num_vote_down": event.downvotes.count(),
                }
            )
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)
        
    def delete(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            if request.user in event.upvotes.all():
                event.upvotes.remove(request.user)
            return response.Response(
                {
                    "num_vote_up": event.upvotes.count(),
                    "num_vote_down": event.downvotes.count(),
                }
            )
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)

class EventDownVoteView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            if request.user not in event.downvotes.all():
                event.downvotes.add(request.user)
                event.upvotes.remove(request.user)
            return response.Response(
                {
                    "num_vote_up": event.upvotes.count(),
                    "num_vote_down": event.downvotes.count(),
                }
            )
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)
        
    def delete(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            if request.user in event.downvotes.all():
                event.downvotes.remove(request.user)
            return response.Response(
                {
                    "num_vote_up": event.upvotes.count(),
                    "num_vote_down": event.downvotes.count(),
                }
            )
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)
        
class EventUpvotedListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EventReadSerializer
    pagination_class = PazeSizePagination
    filterset_class = EventFilter

    def get_queryset(self):
        return Event.objects.filter(upvotes__id=self.request.user.id)