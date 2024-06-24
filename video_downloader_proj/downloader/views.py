import os

from django.http import FileResponse
from django.shortcuts import render
from .forms import LinkTitleForm
from .additional_func import get_format, get_video


def index(request):
    if request.method == 'POST':
        form = LinkTitleForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['title']
            video_data = get_format(url)
            return render(request, 'downloader/index.html', {'form': form, 'video_data': video_data})
    form = LinkTitleForm()
    return render(request, 'downloader/index.html', {'form': form})


def download_video(request):
    if request.method == 'POST':
        url = request.POST.get('url').strip()
        format_video = request.POST.get("format_video").strip()
        file_name = get_video(url, format_video)

        video_file = open(file_name, "rb")
        os.remove(file_name)

        return FileResponse(video_file, as_attachment=True)
