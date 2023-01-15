from uuid import uuid4
import os
from django.db import models
from image.models import Image
from event.models import Event

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

    content = models.TextField(default=None, blank=True, null=True)
    images = models.ManyToManyField(
        Image, related_name='post_images', default=None, blank=True
    )
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='published'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author'
    )
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, default=None, blank=True, null=True
    )
    upvotes = models.ManyToManyField(
        User, related_name="post_upvotes", default=None, blank=True
    )
    downvotes = models.ManyToManyField(
        User, related_name="post_downvotes", default=None, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published = PostPublished()
    draft = PostDraft()

    class Meta:
        ordering = ('-id',)
        
    @property
    def num_vote_up(self):
        return self.upvotes.count()

    @property
    def num_vote_down(self):
        return self.downvotes.count()

    def __str__(self):
        return str(self.author)