from django.urls import path
from .views import AdvertisementListView

app_name = 'advertisement'

urlpatterns = [
    path('', AdvertisementListView.as_view(), name='advertisement'),
]