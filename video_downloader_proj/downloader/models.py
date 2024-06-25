from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from users.models import User


class VideoModel(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=256, unique=True, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    thumbnail = models.ImageField(blank=True, null=True)
    video_formats = models.JSONField()
    add_time = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('video_post', args=[self.pk, self.slug])

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):

        self.slug = slugify(self.title)
        super().save()

    class Meta:
        ordering = ['-add_time']
        indexes = [
            models.Index(fields=['-add_time'])
        ]
