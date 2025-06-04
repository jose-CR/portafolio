from django.db import models

# Create your models here.
class Technology(models.Model):
    name = models.CharField(max_length=200)
    image_technology = models.ImageField(upload_to='technologies', null=True, blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image_project = models.ImageField(upload_to='projects', null=True, blank=True)
    technologies = models.ManyToManyField(Technology, related_name="projects")

    def __str__(self):
        return self.name
