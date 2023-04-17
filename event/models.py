from django.db import models
from tinymce.models import HTMLField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible
from django.utils import timezone

@deconstructible
class RenameAndRelocateImage(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.path, filename)

save_image = RenameAndRelocateImage("images/")

class Event(models.Model):
    title = models.CharField(max_length=50, default=None, blank=True)
    slug = models.SlugField(max_length=50 ,unique=True)
    description = models.TextField()
    ticket_title = models.CharField(max_length=100, default=None, blank=True)
    event_info = HTMLField()
    image = ProcessedImageField(upload_to=save_image,
                                processors=[ResizeToFit(width=1400)],
                                format='JPEG',
                                options={'quality': 80})
    ticket_availability = models.IntegerField(default=0)
    regular_price = models.IntegerField(default=0)
    premium_price = models.IntegerField(default=0)
    regular_features = models.TextField()
    premium_features = models.TextField()
    location = models.CharField(max_length=100, default=None, blank=True)
    google_form_iframe_url = models.URLField(max_length=500)

    event_start_date = models.DateField()
    event_end_date = models.DateField()
    event_time_from = models.TimeField()
    event_time_to = models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    
    def __str__(self):
        return str(self.title)
