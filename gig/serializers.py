from rest_framework import serializers
from .models import Gig
from account.serializers import UserSerializer
from tag.serializers import TagSerializer
from category.serializers import CategorySerializer
from image.serializers import ImageSerializer

class GigWriteSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    num_vote_up = serializers.ReadOnlyField()
    num_vote_down = serializers.ReadOnlyField()
    upvoted = serializers.SerializerMethodField()
    downvoted = serializers.SerializerMethodField()

    class Meta:
        model = Gig
        fields = [
            "id",
            "author",
            "title",
            "description",
            "images",
            "languages",
            "expertises",
            "specializations",
            "tags",
            "category",
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

class GigReadSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    images = ImageSerializer(many=True)
    num_vote_up = serializers.ReadOnlyField()
    num_vote_down = serializers.ReadOnlyField()
    upvoted = serializers.SerializerMethodField()
    downvoted = serializers.SerializerMethodField()
    tags = TagSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Gig
        fields = [
            "id",
            "author",
            "title",
            "description",
            "images",
            "languages",
            "expertises",
            "specializations",
            "tags",
            "category",
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
    
