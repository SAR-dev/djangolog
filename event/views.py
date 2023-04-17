from rest_framework import generics
from .models import Event
from .serializers import EventSerializer
from utils.paginations import PazeSizePagination
from rest_framework import generics, views, response, permissions, exceptions, status
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

class EventListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = EventSerializer
    pagination_class = PazeSizePagination

    def get_queryset(self):
        queryset = Event.objects.all().order_by('event_start_date')
        return queryset

class EventRteriveView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = EventSerializer
    
    def get_object(self):
        try:
            return Event.objects.get(slug=self.kwargs['slug'])
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)

class EventLatestView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = EventSerializer
    
    def get_object(self):
        now = timezone.now()
        try:
            queryset = Event.objects.filter(event_start_date__gte=now)
            return queryset.earliest('event_start_date')
        except Event.DoesNotExist:
            pass
        queryset = Event.objects.filter(event_start_date__lt=now)
        if queryset.exists():
            return queryset.latest('event_start_date')
        raise NotFound(detail="Error 404, Not Found!", code=404)