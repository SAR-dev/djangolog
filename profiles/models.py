from django.db import models
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth import get_user_model
User = get_user_model()

class Profiles(models.Model):
    BLOOD_GROUPS = (
        ("a+", "A+"),
        ("a-", "A-"),
        ("b+", "B+"),
        ("b-", "B_"),
        ("o+", "O+"),
        ("o-", "O-"),
        ("ab+", "AB+"),
        ("ab-", "AB-"),
    )

    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
    )

    author = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=100, null=True, blank=True)
    blood_group = models.CharField(
        max_length=100, null=True, blank=True, choices=BLOOD_GROUPS
    )
    gender = models.CharField(
        max_length=100, null=True, blank=True, choices=GENDER_CHOICES
    )
    contact_email = models.EmailField(
        max_length=60,
        unique=True,
        null=True,
        blank=True,
    )
    contact_number = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                regex="^(\+\d{1,3}[- ]?)?\d{10}$",
                message="Invalid contact number! Use country code too.",
            ),
        ],
    )
    social_links = ArrayField(
        models.CharField(max_length=100, blank=True), size=8, default=list
    )
    location = models.CharField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return str(self.author)
