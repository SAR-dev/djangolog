from rest_framework import serializers
from .models import Order
from package.models import Package
from gig.models import Gig
from account.serializers import UserSerializer

class GigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gig
        fields = [
            "id",
            "title",
        ]

class PackageSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    gig = GigSerializer(read_only=True)

    class Meta:
        model = Package
        fields = [
            "id",
            "author",
            "gig",
            "price",
            "title",
            "description",
            "duration_in_days"
        ]
        read_only_fields = []

class OrderWriteSerializer(serializers.ModelSerializer):
    buyer = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "buyer",
            "package",
            "note",
            "due_on"
        ]
        read_only_fields = []

class OrderReadSerializer(serializers.ModelSerializer):
    buyer = UserSerializer(read_only=True)
    package = PackageSerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "buyer",
            "package",
            "note",
            "due_on",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = []