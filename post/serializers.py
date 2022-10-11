from rest_framework import serializers
from .models import Post
from account.serializers import UserSerializer
from image.serializers import ImageSerializer
from tag.serializers import TagSerializer
from category.serializers import CategorySerializer

class PostSerializer(serializers.ModelSerializer):
    cover = ImageSerializer()
    images = ImageSerializer(many=True)
    tags = TagSerializer(many=True)
    category = CategorySerializer()
    author = UserSerializer()
    
    class Meta:
        model = Post
        fields = ['id','title', 'content', 'category', 'cover', 'images', 'tags', 'status', 'author', 'created_at', 'updated_at']