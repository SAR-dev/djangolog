from django.db import models
from image.models import Image
from django.contrib.postgres.fields import ArrayField
from category.models import Category
from comment.models import Comment
from gig.models import Gig
from django.contrib.auth import get_user_model
User = get_user_model()

class Rating(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE, null=True, blank=True)
    value = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    
    def __str__(self):
        return str(self.title)
