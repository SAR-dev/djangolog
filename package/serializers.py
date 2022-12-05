from rest_framework import serializers
from .models import Package
from account.serializers import UserSerializer

class PackageWriteSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Package
        fields = [
            "id",
            "author",
            "gig",
            "price",
            "title",
            "description",
            "duration_in_days",
            "enabled_services",
            "disabled_services",
            "revisions",
            "created_at",
            "updated_at",
        ]
        read_only_fields = []

class PackageReadSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Package
        fields = [
            "id",
            "author",
            "gig",
            "price",
            "title",
            "description",
            "duration_in_days",
            "enabled_services",
            "disabled_services",
            "revisions",
            "created_at",
            "updated_at",
        ]
        read_only_fields = []