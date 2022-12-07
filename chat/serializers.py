from rest_framework import serializers
from .models import Chat
from account.serializers import UserSerializer

class ChatWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = [
            "id",
            "user_from",
            "user_to",
            "message",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["user_from"]

class ChatReadSerializer(serializers.ModelSerializer):
    user_from = UserSerializer(read_only=True)
    user_to = UserSerializer(read_only=True)

    class Meta:
        model = Chat
        fields = [
            "id",
            "user_from",
            "user_to",
            "message",
            "created_at",
            "updated_at",
        ]
        read_only_fields = []
