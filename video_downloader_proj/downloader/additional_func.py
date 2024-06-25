import yt_dlp

from downloader.models import VideoModel


def get_format(url: str) -> dict:
    """Gather format video info"""
    video_formats = {}
    options = {
        "simulate": True,
    }

    ydl = yt_dlp.YoutubeDL(options)
    video = ydl.extract_info(url=url)
    v_formats = video.get("formats", None)

    for v_format in v_formats:
        format_id = v_format['format_id']
        resolution = v_format.get('resolution', None)
        audio_channels = v_format.get('audio_channels', None)
        print(v_format)

        if v_format['video_ext'] == 'mp4' and resolution:
            if audio_channels:
                video_formats[resolution] = format_id
            resolution = f'Only video - {resolution}'
            video_formats[resolution] = format_id

        if 'audio ' not in video_formats and resolution == 'audio only' and v_format['audio_ext'] == 'm4a':
            video_formats['audio'] = format_id

    title = video.get("title", None)
    thumbnail = video.get("thumbnail", None)

    video_data = {
        "url": url,
        "thumbnail": thumbnail,
        "title": title,
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
