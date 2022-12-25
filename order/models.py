from django.db import models
from package.models import Package
from gig.models import Gig
from django.contrib.postgres.fields import ArrayField
from category.models import Category
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator

User = get_user_model()


class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('late', 'Late'),
        ('cancelled', 'Cancelled'),
    )

    buyer = models.ForeignKey(User, related_name="order_buyer", on_delete=models.DO_NOTHING)
    seller = models.ForeignKey(User, related_name="order_seller", on_delete=models.DO_NOTHING)
    gig = models.ForeignKey(Gig, related_name="order_gig", on_delete=models.DO_NOTHING)
    package = models.ForeignKey(Package, related_name="order_package", on_delete=models.DO_NOTHING)
    note = models.CharField(max_length=350, null=True, blank=True, validators=[MinLengthValidator(15)])
    due_on = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

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
