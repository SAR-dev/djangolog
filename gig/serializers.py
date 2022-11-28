from rest_framework import serializers
from .models import Gig


class GigSerializer(serializers.ModelSerializer):
    languages = serializers.ListField(child=serializers.CharField())
    
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
        read_only_fields = ["author"]
