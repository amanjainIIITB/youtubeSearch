from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.VideoList.as_view(), name='VideoSearch'),
]