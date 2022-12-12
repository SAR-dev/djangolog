from rest_framework import serializers
from .models import Gig
from comment.models import Comment
from account.serializers import UserSerializer
from tag.serializers import TagSerializer
from category.serializers import CategorySerializer
from image.serializers import ImageSerializer
from django.db.models import Avg

class GigWriteSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    num_vote_up = serializers.ReadOnlyField()
    num_vote_down = serializers.ReadOnlyField()
    upvoted = serializers.SerializerMethodField()
    downvoted = serializers.SerializerMethodField()
    total_ratings = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

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
            "total_ratings",
            "average_rating",
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
    
    def get_total_ratings(self, obj):
        return Comment.ratings.filter(gig_id = obj.id).count()
    
    def get_average_rating(self, obj):
        return Comment.ratings.filter(gig_id = obj.id).aggregate(Avg("rating"))

class GigReadSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    images = ImageSerializer(many=True)
    num_vote_up = serializers.ReadOnlyField()
    num_vote_down = serializers.ReadOnlyField()
    upvoted = serializers.SerializerMethodField()
    downvoted = serializers.SerializerMethodField()
    tags = TagSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    total_ratings = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

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
            "total_ratings",
            "average_rating",
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
    
    def get_total_ratings(self, obj):
        return Comment.ratings.filter(gig_id = obj.id).count()
    
    def get_average_rating(self, obj):
        return Comment.ratings.filter(gig_id = obj.id).aggregate(Avg("rating"))
    
