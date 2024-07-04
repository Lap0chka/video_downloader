import yt_dlp

from downloader.models import VideoModel


def get_format(url: str) -> dict:
    """
    Gather format video info

    Args:
        url (str): The URL of the video to extract format information from.

    Returns:
        dict: A dictionary containing the URL, thumbnail, title, and video formats of the extracted video information.
    """
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
    """
    Download a video from a given URL in the specified format.

    Parameters:
        url (str): The URL of the video to download.
        video_format (str): The format in which the video should be downloaded.

    Returns:
        str: The file name of the downloaded video.

    Example:
        get_video("https://www.youtube.com/watch?v=abc123", "mp4")
    """
    options = {
        "format": video_format
    }

    ydl = yt_dlp.YoutubeDL(options)
    video = ydl.extract_info(url=url)
    file_name = ydl.prepare_filename(video)

    return file_name
