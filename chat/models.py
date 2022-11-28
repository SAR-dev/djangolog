from django.db import models
from image.models import Image
from django.contrib.postgres.fields import ArrayField
from category.models import Category
from comment.models import Comment
from gig.models import Gig
from django.contrib.auth import get_user_model
User = get_user_model()

class Chat(models.Model):
    user_from = models.ForeignKey(User, related_name="user_from", on_delete=models.CASCADE)
    user_to = models.ForeignKey(User,related_name="user_to", on_delete=models.CASCADE)
    message = models.CharField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    
    def __str__(self):
        return str(self.message)
