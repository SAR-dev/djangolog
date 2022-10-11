from django.db import models
from image.models import Image
from category.models import Category
from tag.models import Tag
from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    class PostPublished(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    class PostDraft(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='draft')

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    cover = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='cover', default=None, blank=True)
    images = models.ManyToManyField(Image, related_name='images', default=None, blank=True)
    tags = models.ManyToManyField(Tag, related_name='tags', default=None, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', default=None, blank=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published = PostPublished()
    draft = PostDraft()

    class Meta:
        ordering = ('-id',)
        
    def __str__(self):
        return str(self.title)