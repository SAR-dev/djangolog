from rest_framework import serializers
from .models import Gig
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "avatar"]


class GigSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    num_vote_up = serializers.ReadOnlyField()
    num_vote_down = serializers.ReadOnlyField()
    
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
            "upvotes",
            "downvotes",
            "num_vote_up",
            "num_vote_down",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["author"]
