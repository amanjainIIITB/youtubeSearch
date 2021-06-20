from rest_framework.generics import ListAPIView

from .serializer import ContentDetailsSerializer
from .models import ContentDetails

# Create your views here.
class VideoList(ListAPIView):
    queryset = ContentDetails.objects.all().order_by('-publishedAt')
    serializer_class = ContentDetailsSerializer
    filterset_fields = ['title', 'description']