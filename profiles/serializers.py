from rest_framework import serializers
from .models import Profiles

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
            "tagline",
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
            "tagline",
            "languages",
            "facebook",
            "twitter",
            "github",
            "educations",
            "certifications",
            "created_at",
            "updated_at",
        ]
        read_only_fields = []
    
