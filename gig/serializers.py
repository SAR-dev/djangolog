from rest_framework import serializers
from .models import Gig
from package.models import Package
from comment.models import Comment
from account.serializers import UserSerializer, UserWithRatingsSerializer
from category.serializers import CategorySerializer
from image.serializers import ImageSerializer
from django.db.models import Avg
from package.serializers import PackageReadSerializer

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
            "faq",
            "extra_services",
            "videos",
            "documents",
            "requirements",
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
    author = UserWithRatingsSerializer(read_only=True)
    images = ImageSerializer(many=True)
    num_vote_up = serializers.ReadOnlyField()
    num_vote_down = serializers.ReadOnlyField()
    upvoted = serializers.SerializerMethodField()
    downvoted = serializers.SerializerMethodField()
    category = CategorySerializer(read_only=True)
    total_ratings = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    packages = serializers.SerializerMethodField()

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
            "faq",
            "extra_services",
            "videos",
            "documents",
            "requirements",
            "num_vote_up",
            "num_vote_down",
            "upvoted",
            "downvoted",
            "total_ratings",
            "average_rating",
            "packages",
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
    
    def get_packages(self, obj):
        objects = PackageReadSerializer(data=Package.objects.filter(gig_id=obj.id), many=True)
        objects.is_valid()
        return objects.data
    
