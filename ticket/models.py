from django.db import models
from event.models import Event
from paythod.models import Paythod
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

class Ticket(models.Model):  
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    code = models.CharField(max_length=50, unique=True,  validators=[MinValueValidator(10)])
    method = models.ForeignKey(Paythod, on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.author)
