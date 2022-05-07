from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save , post_delete
from users.models import *


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def createProfile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_delete,sender=Profile)
def DeleteUser(sender,instance,**kwargs):
    instance.user.delete()