# Generated by Django 3.2.25 on 2025-03-25 00:17

from django.db import migrations, models
import project.models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_image',
        ),
        migrations.AddField(
            model_name='project',
            name='project_image_url',
            field=models.ImageField(blank=True, null=True, upload_to=project.models.random_filename),
        ),
    ]
