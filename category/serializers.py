from rest_framework import serializers
from .models import Category
from gig.models import Gig
from comment.models import Comment
from account.serializers import UserSerializer
from image.serializers import ImageSerializer
from tag.serializers import TagSerializer
from django.db.models import Avg

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'label', 'color', 'slug']

class CategoryFeedSerializer(serializers.ModelSerializer):
    gigs = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'name',  'label', 'slug', 'color', 'gigs']

    def get_gigs(self, obj):
        objects = GigFeedSerializer(data=Gig.objects.filter(category_id=obj.id)[:8], many=True, context={'request': self.context.get('request')})
        objects.is_valid()
        return objects.data

class GigFeedSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    images = ImageSerializer(many=True)
    num_vote_up = serializers.ReadOnlyField()
    num_vote_down = serializers.ReadOnlyField()
    upvoted = serializers.SerializerMethodField()
    downvoted = serializers.SerializerMethodField()
    tags = TagSerializer(read_only=True, many=True)
    total_ratings = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Gig
        fields = [
            "id",
            "author",
            "title",
            "images",
            "tags",
            "category",
            "gig",
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
    
