from django.shortcuts import render
from .models import Chat
from .serializers import ChatWriteSerializer, ChatReadSerializer
from rest_framework import generics, views, response, permissions, exceptions, status
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist
from django_filters import rest_framework as filters
from utils.paginations import PazeSizePagination
from django.db.models import Q
from django.core import serializers
from account.serializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class IsChatAuthor(permissions.BasePermission):
    message = 'You can not view this route!'

    def has_permission(self, request, view):
        try:
            chat = Chat.objects.get(pk=view.kwargs.get('pk'))
            author = chat.user_from == request.user
            return author
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)
        
class IsChatParticipant(permissions.BasePermission):
    message = 'You can not view this route!'

    def has_permission(self, request, view):
        try:
            chat = Chat.objects.get(pk=view.kwargs.get('pk'))
            author = chat.user_from == request.user or chat.user_to == request.user
            return author
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)
        
class ChatFilter(filters.FilterSet):
    o = filters.OrderingFilter(
        fields=(
            ('created_at', 'created_at'),
        ),
    )
    class Meta:
        model = Chat
        fields = {
            'user_from__id': ['exact'],
            'user_to__id': ['exact']
        }

class ChatCreateView(generics.CreateAPIView):
    def perform_create(self, serializer):
        serializer.save(user_from=self.request.user)

    permission_classes = [permissions.IsAuthenticated]
    queryset = Chat.objects.all()
    serializer_class = ChatWriteSerializer
    pagination_class = PazeSizePagination
    filterset_class = ChatFilter

class MyChatListView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            users = Chat.objects.filter(Q(user_from=self.request.user) | Q(user_to=self.request.user)).values_list('user_to', flat=True).distinct()
            queryset = []
            for user in users:
                queryset.append(User.objects.get(id=user))
            serializer = UserSerializer(queryset, many=True)
            return response.Response(serializer.data)
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)

class ChatRetriveView(generics.RetrieveAPIView):
    permission_classes = [IsChatParticipant]
    queryset = Chat.objects.all()
    serializer_class = ChatReadSerializer

class ChatUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsChatAuthor]
    queryset = Chat.objects.all()
    serializer_class = ChatWriteSerializer

