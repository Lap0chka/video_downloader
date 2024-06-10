import yt_dlp


def get_format(url: str) -> dict:
    """We don't download video. We gather format video info"""
    video_formats = {}
    options = {
        "simulate": True,
    }

    ydl = yt_dlp.YoutubeDL(options)
    video = ydl.extract_info(url=url)
    v_formats = video.get("formats", None)

    for v_format in v_formats:

        resolution = v_format['format']
        format_video = v_format['video_ext']
        if format_video == 'none':
            format_video = 'audio'
        video_formats[format_video] = resolution

    video_data = {
        "url": url,
        "thumbnail": video.get("thumbnail", None),
        "title": video.get("title", None),
        "video_formats": video_formats
    }

    return video_data


def get_video(url, video_format):

    options = {
        "format": video_format
    }

    ydl = yt_dlp.YoutubeDL(options)
    video = ydl.extract_info(url=url)
    file_name = ydl.prepare_filename(video)

    return file_name


