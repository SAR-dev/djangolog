from rest_framework import serializers
from .models import Category
from gig.models import Gig
from account.serializers import UserSerializer
from image.serializers import ImageSerializer
from tag.serializers import TagSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class CategoryFeedSerializer(serializers.ModelSerializer):
    gigs = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

    def get_gigs(self, obj):
        objects = GigReadSerializer(data=Gig.objects.filter(category_id=obj.id)[:10], many=True)
        objects.is_valid()
        return objects.data

class GigReadSerializer(serializers.ModelSerializer):
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
        return obj.upvotes.filter(pk=self.context.get('request').user.id).exists()
    
    def get_downvoted(self, obj):
        return obj.downvotes.filter(pk=self.context.get('request').user.id).exists()
    
    def get_total_ratings(self, obj):
        return Comment.ratings.filter(gig_id = obj.id).count()
    
    def get_average_rating(self, obj):
        return Comment.ratings.filter(gig_id = obj.id).aggregate(Avg("rating"))
    
