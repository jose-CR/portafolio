import os
from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

def random_filename(instance, filename):
    extension = filename.split('.')[-1]
    new_name = f"{uuid4().hex}.{extension}"
    return os.path.join('projects/img/', new_name)

# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=30)
    project_description = models.CharField(max_length=120)
    project_image_url = models.ImageField(upload_to=random_filename, null=True, blank=True)
    
    def __str__(self):
        return self.project_name
