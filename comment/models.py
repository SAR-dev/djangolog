from django.db import models
from gig.models import Gig
from django.contrib.auth import get_user_model
User = get_user_model()

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

    upvotes = models.ManyToManyField(User, related_name="upvotes", default=None, blank=True)
    downvotes = models.ManyToManyField(User, related_name="downvotes", default=None, blank=True)

    gig = models.ForeignKey(Gig, related_name="gig", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    
    def __str__(self):
        return str(self.message[:30])
