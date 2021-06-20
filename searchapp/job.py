from apscheduler.schedulers.background import BackgroundScheduler

from apiclient.discovery import build
import youtubeSearch.settings
from .models import ContentDetails


def scheduler_get_latest_youtube_video():
    try:
        youtube_resource = build('youtube', 'v3', developerKey=youtubeSearch.settings.YOUTUBE_API_KEY)
        request = youtube_resource.search().list(q='Gaming', part='snippet', type='video', order='date', publishedAfter='2021-06-18T04:15:00Z', maxResults=5)
        response = request.execute()
        items = response['items']
        for item in items:
            if ContentDetails.objects.filter(videoID=item['id']['videoId']).exists()==False:
                ContentDetails(videoID=item['id']['videoId'], publishedAt=item['snippet']['publishedAt'],
                               title=item['snippet']['title'], description=item['snippet']['description'],
                               thumbnail_url=item['snippet']['thumbnails']['default']['url']).save()
    except:
        error_info = 'Please check below points\n'
        error_info = error_info + 'Please check your internet connection\n'
        error_info = error_info + 'Please make sure Youtube API is not expired.\n'
        error_info = error_info + 'Youtube provides only 10k videos information, make sure you have not exhausted the limit.'
        print(error_info)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduler_get_latest_youtube_video, 'interval', seconds=10)
    scheduler.start()
