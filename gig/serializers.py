from rest_framework import serializers
from .models import Gig


class GigSerializer(serializers.ModelSerializer):
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
            "created_at",
            "updated_at"
        ]
