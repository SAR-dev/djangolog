from django.db import models
from image.models import Image
from django.contrib.postgres.fields import ArrayField
from category.models import Category
from django.contrib.auth import get_user_model

User = get_user_model()


class Gig(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField()
    images = models.ManyToManyField(
        Image, related_name="gig_images", blank=True
    )
    languages = ArrayField(
        models.CharField(max_length=100, blank=True), size=8, default=list
    )
    expertises = ArrayField(
        models.CharField(max_length=100, blank=True), size=8, default=list
    )
    specializations = ArrayField(
        models.CharField(max_length=100, blank=True), size=8, default=list
    )
    tags = ArrayField(
        models.CharField(max_length=20, blank=True), size=8, default=list
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="gig_category",
        default=None,
        blank=True,
    )
    faq = ArrayField(
        models.CharField(max_length=500, blank=True), size=20, default=list
    )
    extra_services = ArrayField(
        models.CharField(max_length=100, blank=True), size=8, default=list
    )
    videos = ArrayField(
        models.CharField(max_length=200, blank=True), size=8, default=list
    )
    documents = ArrayField(
        models.CharField(max_length=200, blank=True), size=8, default=list
    )
    requirements = ArrayField(
        models.CharField(max_length=500, blank=True), size=8, default=list
    )

    upvotes = models.ManyToManyField(User, related_name="gig_upvotes",  default=None, blank=True)
    downvotes = models.ManyToManyField(User, related_name="gig_downvotes",  default=None, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    @property
    def num_vote_up(self):
        return self.upvotes.count()

    @property
    def num_vote_down(self):
        return self.downvotes.count()

    def __str__(self):
        return str(self.title)
