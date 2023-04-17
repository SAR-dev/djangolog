from django.urls import path
from .views import EventListView, EventRteriveView, EventLatestView

app_name = 'event'

urlpatterns = [
	path('list/', EventListView.as_view(), name='event-list'),
	path('latest/', EventLatestView.as_view(), name='event-list'),
	path('<str:slug>/', EventRteriveView.as_view(), name='event-read'),
]