from rest_framework import serializers
from .models import Image
from django.contrib.auth import get_user_model
User = get_user_model()
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'height', 'width']
        
class ImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'description']
        
class ImageRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'height', 'width', 'author']
        
class ImageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'description']