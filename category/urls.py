from django.urls import path
from .views import CategoryListView, CategoryFeedListView, CategoryFeedRtriveView

app_name = 'category'

urlpatterns = [
	path('', CategoryListView.as_view(), name='category-list'),
	path('feed/list/', CategoryFeedListView.as_view(), name='category-feed'),
	path('feed/<pk>/', CategoryFeedRtriveView.as_view(), name='category-feed-read'),
]