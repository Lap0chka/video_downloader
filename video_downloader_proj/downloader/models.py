from django.db import models


class VideoModel(models.Model):
    title = models.CharField()
    url = models.URLField()
    thumbnail = models.ImageField(blank=True, null=True)
    video_formats = models.JSONField()

