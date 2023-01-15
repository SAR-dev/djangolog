from rest_framework import serializers
from .models import Post
from account.serializers import UserSerializer

class PostWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "content",
            "images",
            "status",
            "event",
        ]
        read_only_fields = []

class PostReadSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    upvoted = serializers.SerializerMethodField()
    downvoted = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "content",
            "images",
            "status",
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
    
