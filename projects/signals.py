import os 
from .models import Technology
from django.dispatch import receiver
from django.db.models.signals import post_delete

@receiver(post_delete, sender=Technology)
def delete_image_file(sender, instance, **kwargs):
    if instance.image_technology and os.path.isfile(instance.image_technology.path):
        os.remove(instance.image_technology.path)