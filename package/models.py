from django.db import models
from event.models import Event
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.postgres.fields import ArrayField

from django.contrib.auth import get_user_model
User = get_user_model()

class Package(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=15, validators=[MinLengthValidator(1)])
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    facilities = ArrayField(
        models.CharField(max_length=100, blank=True), size=8, default=list
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.name)