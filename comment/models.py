from django.db import models
from gig.models import Gig
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class Comment(models.Model):
    class CommentWithoutRating(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(rating__isnull = True)
        
    class CommentWithRating(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(rating__isnull = False)
        
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    rating = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)], null=True, blank=True
    )
    upvotes = models.ManyToManyField(
        User, related_name="upvotes", default=None, blank=True
    )
    downvotes = models.ManyToManyField(
        User, related_name="downvotes", default=None, blank=True
    )

    gig = models.ForeignKey(Gig, related_name="gig", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    comments = CommentWithoutRating()
    ratings = CommentWithRating()

    def __str__(self):
        return str(self.message[:30])
