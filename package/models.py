from django.db import models
from django.contrib.postgres.fields import ArrayField
from gig.models import Gig
from django.contrib.auth import get_user_model
User = get_user_model()

class Package(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE)
    price = models.IntegerField()
    title = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField()
    duration_in_days = models.IntegerField()
    enabled_services = ArrayField(
        models.CharField(max_length=100, blank=True), size=8, default=list
    )
    disabled_services = ArrayField(
        models.CharField(max_length=100, blank=True), size=8, default=list
    )
    revisions = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    
    def __str__(self):
        return str(self.title)
