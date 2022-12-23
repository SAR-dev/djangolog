from rest_framework import serializers
from .models import Package
from account.serializers import UserSerializer

class PackageBulkCreateSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        package_data = [Package(**item) for item in validated_data]
        return Package.objects.bulk_create(package_data)
    
class PackageWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = [
            "gig",
            "price",
            "title",
            "description",
            "duration_in_days",
            "revisions",
            "prototype",
            "content_upload",
            "source_file",
            "consulatation",
            "deployment",
            "integration",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id"]
        list_serializer_class = PackageBulkCreateSerializer

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
            "revisions",
            "prototype",
            "content_upload",
            "source_file",
            "consulatation",
            "deployment",
            "integration",
            "created_at",
            "updated_at",
        ]
        read_only_fields = []


