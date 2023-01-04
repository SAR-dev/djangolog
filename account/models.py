import os
from uuid import uuid4
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.core.validators import RegexValidator
from django.db import models
from django.utils.deconstruct import deconstructible
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


@deconstructible
class RenameAndRelocateImage(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.path, filename)
rename_and_relocate_avatar = RenameAndRelocateImage("images/avatar/")


class AccountManager(BaseUserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(
            self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})

    def create_user(self, email, first_name, last_name, username, password=None):
        if not email:
            raise ValueError('Email address is required')
        if not first_name:
            raise ValueError('First name is required')
        if not last_name:
            raise ValueError('Last name is required')
        if not username:
            raise ValueError('Username is required')
        user = self.model(email=self.normalize_email(email),
                          first_name=first_name, last_name=last_name, username=username)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, username, password):
        user = self.create_user(email=self.normalize_email(email),
                                first_name=first_name, last_name=last_name, username=username,
                                password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=60, unique=True)
    username = models.CharField(max_length=50, unique=True, validators=[
        RegexValidator(
            regex='^[a-zA-Z0-9\d](?:[a-zA-Z0-9\d]|-(?=[a-zA-Z0-9\d])){0,50}$',
            message="Username should be between 3-50 lowecase characters. Use hyphen '-' between letters if needed. ",
        ),
    ])
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    avatar = ProcessedImageField(upload_to=rename_and_relocate_avatar,
                                 default='images/avatar.jpg',
                                 processors=[ResizeToFit(width=200)],  # type: ignore
                                 format='JPEG',  # type: ignore
                                 options={'quality': 60})  # type: ignore
    
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    
    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    def __str__(self):
        return str(self.username)

    class Meta:
       ordering = ['-id']

