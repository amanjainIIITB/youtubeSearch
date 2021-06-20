from rest_framework.views import APIView
from rest_framework.response import Response

from apiclient.discovery import build
import youtubeSearch.settings

# Create your views here.
class VideoSearch(APIView):
    def get(self, request):
        youtube_resource = build('youtube', 'v3', developerKey=youtubeSearch.settings.YOUTUBE_API_KEY)
        request = youtube_resource.search().list(q='', part='snippet', type='video')
        response = request.execute()
        return Response(response)