from django.urls import path
from . import views

app_name = 'downloader'

urlpatterns = [
    path('', views.index, name='index'),
    path('post_video/<int:pk>/<slug:video_slug>/', views.video_post, name='video_post'),
    path('download_video/', views.download_video, name='download'),
]
