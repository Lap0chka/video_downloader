# Generated by Django 5.0.6 on 2024-06-25 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloader', '0002_videomodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videomodel',
            name='slug',
            field=models.SlugField(max_length=256, unique=True),
        ),
    ]
