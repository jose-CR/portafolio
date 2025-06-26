from django.db import models
from django.contrib.auth.models import AbstractUser
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class UserProfile(AbstractUser):
    description = CKEditor5Field('Description', config_name='default', blank=True, null=True)
    github = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)

class ContactMe(models.Model):
    user_name = models.CharField(max_length=50, blank=True, null=True)
    user_email = models.EmailField(blank=True, null=True)
    user_message = CKEditor5Field('Message', config_name="default", blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.created_at.strftime('%Y-%m-%d')}"

class AboutPageConfig(models.Model):
    featured_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Perfil destacado: {self.featured_profile.username}"
