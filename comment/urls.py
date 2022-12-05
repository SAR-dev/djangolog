from django.urls import path
from .views import CommentCreateView, CommentListView, CommentRetriveView, CommentUpdateDestroyView

app_name = 'comment'

urlpatterns = [
    path('', CommentCreateView.as_view(), name='comment-create'),
    path('', CommentListView.as_view(), name='comment-list'),
    path('<pk>/', CommentRetriveView.as_view(), name='comment-retrive'),
    path('<pk>/', CommentUpdateDestroyView.as_view(), name='comment-update-destroy'),
]