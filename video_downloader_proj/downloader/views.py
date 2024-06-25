import os

from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.shortcuts import render, get_object_or_404
from .forms import LinkTitleForm
from .additional_func import get_format, get_video
from .models import VideoModel


def index(request):
    videos = VideoModel.objects.all()
    if request.method == 'POST':
        form = LinkTitleForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['title']

            video_data = get_format(url)
            if request.user.is_authenticated:
                VideoModel.objects.create(
                    title=video_data['title'], user=request.user,
                    url=video_data['url'], thumbnail=video_data['thumbnail'],
                    video_formats=video_data['video_formats']
                )
            return render(request, 'downloader/index.html',
                          {'form': form, 'video_data': video_data})
    form = LinkTitleForm()
    return render(request, 'downloader/index.html', {'form': form, 'videos': videos})


def download_video(request):
    if request.method == 'POST':
        url = request.POST.get('url').strip()
        format_video = request.POST.get("format_video").strip()
        file_name = get_video(url, format_video)

        video_file = open(file_name, "rb")
        os.remove(file_name)

        return FileResponse(video_file, as_attachment=True)


@login_required
def video_post(request, video_pk, video_slug):
    post = get_object_or_404(VideoModel, pk=video_pk, slug=video_slug)
    return render(request, 'downloader/video_post.html', {'post': post})
