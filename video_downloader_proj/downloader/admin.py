from django.contrib import admin

from downloader.models import VideoModel


@admin.register(VideoModel)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']
