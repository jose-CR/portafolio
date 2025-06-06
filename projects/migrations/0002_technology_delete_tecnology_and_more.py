# Generated by Django 5.2.1 on 2025-06-02 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image_tecnology', models.ImageField(blank=True, null=True, upload_to='technologies')),
            ],
        ),
        migrations.DeleteModel(
            name='Tecnology',
        ),
        migrations.AlterField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(related_name='projects', to='projects.technology'),
        ),
    ]
