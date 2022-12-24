from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible

@deconstructible
class RenameAndRelocateImage(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.path, filename)

save_image = RenameAndRelocateImage("images/")

class Advertisement(models.Model):
    title = models.CharField(max_length=50, default=None, blank=True)
    subtitle = models.CharField(max_length=150, default=None, blank=True)
    url = models.URLField(max_length=300)
    image = ProcessedImageField(upload_to=save_image,
                                processors=[ResizeToFit(width=1400)],
                                format='JPEG',
                                options={'quality': 80})

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    
    def __str__(self):
        return str(self.subject)
