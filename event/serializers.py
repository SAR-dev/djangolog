from rest_framework import serializers
from .models import Event
from account.serializers import UserSerializer
from image.serializers import ImageSerializer
from category.serializers import CategorySerializer

class EventReadSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    cover = ImageSerializer()
    images = ImageSerializer(many=True)
    category = CategorySerializer()
    num_vote_up = serializers.ReadOnlyField()
    num_vote_down = serializers.ReadOnlyField()
    upvoted = serializers.SerializerMethodField()
    downvoted = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            "id",
            "author",
            "name",
            "description",
            "start_at",
            "finish_at",
            "cover",
            "images",
            "category",
            "location_name",
            "location_link",
            "tags",
            "faq",
            "services",
            "facilities",
            "rules",
            "videos",
            "requirements",
            "status",
            "type",
            "num_vote_up",
            "num_vote_down",
            "upvoted",
            "downvoted",
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

class EventWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "name",
            "description",
            "start_at",
            "finish_at",
            "cover",
            "images",
            "category",
            "location_name",
            "location_link",
            "tags",
            "faq",
            "services",
            "facilities",
            "rules",
            "videos",
            "requirements",
            "status",
            "type",
        ]
        read_only_fields = []