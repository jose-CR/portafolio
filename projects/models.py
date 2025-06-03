import os
from django.db import models

# Create your models here.
class Technology(models.Model):
    name = models.CharField(max_length=200)
    image_technology = models.ImageField(upload_to='technologies', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            old_instance = Technology.objects.get(pk=self.pk)
            if old_instance.image_technology and os.path.isfile(old_instance.image_technology.path):
                os.remove(old_instance.image_technology.path)
        except Technology.DoesNotExist:
            pass
        super().save(*args, **kwargs)

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image_project = models.ImageField(upload_to='media/projects', null=True, blank=True)
    technologies = models.ManyToManyField(Technology, related_name="projects")

    def __str__(self):
        return self.name
