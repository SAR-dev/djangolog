from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from comment.models import Comment
from profiles.models import Profiles
from django.db.models import Avg
from profiles.serializers import ProfilesReadSerializer
User = get_user_model()

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'avatar']

class UserAvatarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['avatar']

class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "avatar"]
    
class UserWithRatingsSerializer(serializers.ModelSerializer):
    total_ratings = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "avatar", "total_ratings", "average_rating", "created_at", "updated_at", "profile"]

    def get_total_ratings(self, obj):
        return Comment.ratings.filter(gig__author_id = obj.id).count()
    
    def get_average_rating(self, obj):
        return Comment.ratings.filter(gig__author_id = obj.id).aggregate(Avg("rating"))
    
    def get_profile(self, obj):
        objects = ProfilesReadSerializer(data=Profiles.objects.filter(author_id = obj.id), many=True)
        objects.is_valid()
        return objects.data[0]
    