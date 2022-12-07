from django.urls import path
from .views import ChatCreateView, MyChatListView, ChatRetriveView, ChatUpdateDestroyView

app_name = 'chat'

urlpatterns = [
    path('', ChatCreateView.as_view(), name='chat-create'),
    path('list/', MyChatListView.as_view(), name='chat-list'),
    path('<pk>/', ChatRetriveView.as_view(), name='chat-retrive'),
    path('<pk>/update/', ChatUpdateDestroyView.as_view(), name='chat-update-destroy'),
]