from django.urls import path
from .views import GigCreateView, GigListView, GigSearchView, GigRetriveView, GigUpdateDestroyView, GigUpVoteView, GigDownVoteView, GigUpvotedListView

app_name = 'gig'

urlpatterns = [
    path('', GigCreateView.as_view(), name='gig-create'),
    path('list/', GigListView.as_view(), name='gig-list'),
    path('search/<str:keyword>/', GigSearchView().as_view(), name='gig-search'),
    path('upvoted/', GigUpvotedListView.as_view(), name='gig-upvoted-list'),
    path('<pk>/', GigRetriveView.as_view(), name='gig-retrive'),
    path('<pk>/update/', GigUpdateDestroyView.as_view(), name='gig-update-destroy'),
    path('<int:pk>/vote/up/', GigUpVoteView.as_view(), name='gig-upvote'),
    path('<int:pk>/vote/down/', GigDownVoteView.as_view(), name='gig-downvote'),
]