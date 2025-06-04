import os 
from .models import Technology, Project
from django.dispatch import receiver
from django.db.models.signals import post_delete, pre_save

@receiver(post_delete, sender=Technology)
def delete_image_file(sender, instance, **kwargs):
    if instance.image_technology and os.path.isfile(instance.image_technology.path):
        os.remove(instance.image_technology.path)

@receiver(pre_save, sender=Technology)
def delete_old_image_on_change_technology(sender, instance, **kwargs):
    if not instance.pk:
        # Es un nuevo objeto, nada que borrar
        return

    try:
        old_instance = Technology.objects.get(pk=instance.pk)
    except Technology.DoesNotExist:
        return

    old_image = old_instance.image_technology
    new_image = instance.image_technology

    # Si la imagen cambió, elimina la vieja del sistema de archivos
    if old_image and old_image != new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)

@receiver(post_delete, sender=Project)
def delete_image_file_project(sender, instance, **kwargs):
    if instance.image_project and os.path.isfile(instance.image_project.path):
        os.remove(instance.image_project.path)

@receiver(pre_save, sender=Project)
def delete_old_image_on_change_project(sender, instance, **kwargs):
    if not instance.pk:
        # Es un nuevo objeto, nada que borrar
        return

    try:
        old_instance = Project.objects.get(pk=instance.pk)
    except Project.DoesNotExist:
        return

    old_image = old_instance.image_project
    new_image = instance.image_project

    # Si la imagen cambió, elimina la vieja del sistema de archivos
    if old_image and old_image != new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)