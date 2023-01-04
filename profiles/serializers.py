from rest_framework import serializers
from .models import Profiles
from account.serializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()
   
class ProfilesWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = [
            "id",
            "author",
            "nick_name",
            "blood_group",
            "gender",
            "contact_email",
            "contact_number",
            "social_links",
            "location",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["author"]

class ProfilesReadSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    author = UserSerializer(read_only=True)

    class Meta:
        model = Profiles
        fields = [
            "id",
            "author",
            "nick_name",
            "blood_group",
            "gender",
            "contact_email",
            "contact_number",
            "social_links",
            "location",
            "owner",
            "created_at",
            "updated_at",
        ]
        read_only_fields = []

    def get_owner(self, obj):
        try:
            return obj.author == self.context.get('request').user
        except:
            return False