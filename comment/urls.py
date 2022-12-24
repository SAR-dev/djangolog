from django.urls import path
from .views import CommentCreateView, CommentListView, CommentRetriveView, CommentUpdateDestroyView, CommentUpVoteView, CommentDownVoteView

app_name = 'comment'

urlpatterns = [
    path('', CommentCreateView.as_view(), name='comment-create'),
    path('list/', CommentListView.as_view(), name='comment-list'),
    path('<pk>/', CommentRetriveView.as_view(), name='comment-retrive'),
    path('<pk>/update/', CommentUpdateDestroyView.as_view(), name='comment-update-destroy'),
    path('<int:pk>/vote/up/', CommentUpVoteView.as_view(), name='comment-upvote'),
    path('<int:pk>/vote/down/', CommentDownVoteView.as_view(), name='comment-downvote'),
]