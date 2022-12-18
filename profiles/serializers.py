from rest_framework import serializers
from .models import Profiles
from comment.models import Comment
from django.db.models import Avg
from django.contrib.auth import get_user_model
User = get_user_model()
   
class UserProfileSerializer(serializers.ModelSerializer):
    total_ratings = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "avatar", "total_ratings", "average_rating", "date_joined"]

    def get_total_ratings(self, obj):
        return Comment.ratings.filter(gig__author_id = obj.id).count()
    
    def get_average_rating(self, obj):
        return Comment.ratings.filter(gig__author_id = obj.id).aggregate(Avg("rating"))
    

class ProfilesWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = [
            "id",
            "author",
            "nick_name",
            "bio",
            "quote",
            "blood_group",
            "gender",
            "contact_email",
            "contact_number",
            "website",
            "location",
            "languages",
            "facebook",
            "twitter",
            "github",
            "educations",
            "certifications",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["author"]

class ProfilesReadSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    author = UserProfileSerializer(read_only=True)

    class Meta:
        model = Profiles
        fields = [
            "id",
            "author",
            "nick_name",
            "bio",
            "quote",
            "blood_group",
            "gender",
            "contact_email",
            "contact_number",
            "website",
            "location",
            "languages",
            "facebook",
            "twitter",
            "github",
            "educations",
            "certifications",
            "owner",
            "created_at",
            "updated_at",
        ]
        read_only_fields = []

    def get_owner(self, obj):
        return obj.author == self.context.get('request').user
 