from rest_framework import serializers
from .models import Comment
from account.serializers import UserSerializer

class CommentWriteSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    upvoted = serializers.SerializerMethodField()
    downvoted = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "author",
            "message",
            "rating",
            "event",
            "num_vote_up",
            "num_vote_down",
            "upvoted",
            "downvoted",
            "created_at",
            "updated_at",
        ]
        read_only_fields = []

    def get_upvoted(self, obj):
        return obj.upvotes.filter(pk=self.context.get('request').user.id).exists()
    
    def get_downvoted(self, obj):
        return obj.downvotes.filter(pk=self.context.get('request').user.id).exists()

class CommentReadSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    upvoted = serializers.SerializerMethodField()
    downvoted = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "author",
            "message",
            "rating",
            "event",
            "num_vote_up",
            "num_vote_down",
            "upvoted",
            "downvoted",
            "created_at",
            "updated_at",
        ]
        read_only_fields = []

    def get_upvoted(self, obj):
        try:
            return obj.upvotes.filter(pk=self.context.get('request').user.id).exists()
        except:
            return False
    
    def get_downvoted(self, obj):
        try:
            return obj.downvotes.filter(pk=self.context.get('request').user.id).exists()
        except:
            return False
    
