from django.urls import path
from .views import PostCreateView, PostListView, PostRetriveView, PostUpdateDestroyView, PostUpVoteView, PostDownVoteView

app_name = 'post'

urlpatterns = [
    path('', PostCreateView.as_view(), name='post-create'),
    path('list/', PostListView.as_view(), name='post-list'),
    path('<pk>/', PostRetriveView.as_view(), name='post-retrive'),
    path('<pk>/update/', PostUpdateDestroyView.as_view(), name='post-update-destroy'),
    path('<int:pk>/vote/up/', PostUpVoteView.as_view(), name='post-upvote'),
    path('<int:pk>/vote/down/', PostDownVoteView.as_view(), name='post-downvote'),
]