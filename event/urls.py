from django.urls import path
from .views import EventCreateView, EventListView, EventSearchView, EventRetriveView, EventUpdateDestroyView, EventUpVoteView, EventDownVoteView, EventUpvotedListView

app_name = 'event'

urlpatterns = [
    path('', EventCreateView.as_view(), name='event-create'),
    path('list/', EventListView.as_view(), name='event-list'),
    path('search/<str:keyword>/', EventSearchView().as_view(), name='event-search'),
    path('upvoted/', EventUpvotedListView.as_view(), name='event-upvoted-list'),
    path('<pk>/', EventRetriveView.as_view(), name='event-retrive'),
    path('<pk>/update/', EventUpdateDestroyView.as_view(), name='event-update-destroy'),
    path('<int:pk>/vote/up/', EventUpVoteView.as_view(), name='event-upvote'),
    path('<int:pk>/vote/down/', EventDownVoteView.as_view(), name='event-downvote'),
]