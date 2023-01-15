from django.db import models
from image.models import Image
from category.models import Category
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinLengthValidator, MaxLengthValidator

from django.contrib.auth import get_user_model
User = get_user_model()

class Event(models.Model):
    class Published(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    class Draft(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='draft')

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    TYPE_CHOICES = (
        ('free', 'Free'),
        ('paid', 'Paid'),
        ('limited', 'Limited'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, validators=[MinLengthValidator(15)])
    description = models.TextField()
    start_at=models.DateTimeField()
    finish_at=models.DateTimeField()
    cover = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True)
    images = models.ManyToManyField(Image, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        default=None,
        blank=True,
    )
    location_name=models.CharField(max_length=100, validators=[MinLengthValidator(5)])
    location_link=models.URLField(max_length=300, null=True, blank=True)

    tags = ArrayField(
        models.CharField(max_length=20, blank=True), size=20, default=list
    )
    faq = ArrayField(
        models.CharField(max_length=500, blank=True), size=20, default=list
    )
    services = ArrayField(
        models.CharField(max_length=100, blank=True), size=8, default=list
    )
    facilities = ArrayField(
        models.CharField(max_length=100, blank=True), size=8, default=list
    )
    rules = ArrayField(
        models.CharField(max_length=100, blank=True), size=8, default=list
    )
    videos = ArrayField(
        models.URLField(max_length=200, blank=True), size=8, default=list
    )
    requirements = ArrayField(
        models.CharField(max_length=500, blank=True), size=8, default=list
    )

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='published')
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='free')

    upvotes = models.ManyToManyField(User, related_name="gig_upvotes",  default=None, blank=True)
    downvotes = models.ManyToManyField(User, related_name="gig_downvotes",  default=None, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published = Published()
    draft = Draft()

    @property
    def num_vote_up(self):
        return self.upvotes.count()

    @property
    def num_vote_down(self):
        return self.downvotes.count()

    def __str__(self):
        return str(self.name)