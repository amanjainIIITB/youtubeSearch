from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.VideoSearch.as_view(), name='VideoSearch'),
]