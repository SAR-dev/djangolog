from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Account
from profiles.models import Profiles
from django.contrib.auth import get_user_model
User = get_user_model()

@receiver(post_save, sender=User)
def create_related(sender, instance, created, *args, **kwargs):
    if instance and created:
        instance.profiles = Profiles.objects.create(author=instance)

@receiver(pre_save, sender=Account)
def save(sender, instance, *args, **kwargs):
    if instance.avatar:
        try:
            acc = Account.objects.get(id=instance.id)
            pre = acc.avatar
            post = instance.avatar
            if (pre != post and pre != "images/avatar.jpg"):
                pre.delete(save=True)
        except:
            pass