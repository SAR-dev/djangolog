from django.urls import path
from gig.views import GigCreateView, GigListView, GigRetriveView, GigUpdateDestroyView

app_name = 'gig'

urlpatterns = [
    path('', GigCreateView.as_view(), name='gig-list-create'),
    path('', GigListView.as_view(), name='gig-list-create'),
    path('<pk>/', GigRetriveView.as_view(), name='gig-retrive-update-destroy'),
    path('<pk>/', GigUpdateDestroyView.as_view(), name='gig-retrive-update-destroy'),
]