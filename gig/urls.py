from django.urls import path
from .views import GigCreateView, GigListView, GigRetriveView, GigUpdateDestroyView

app_name = 'gig'

urlpatterns = [
    path('', GigCreateView.as_view(), name='gig-create'),
    path('list/', GigListView.as_view(), name='gig-list'),
    path('<pk>/', GigRetriveView.as_view(), name='gig-retrive'),
    path('<pk>/update/', GigUpdateDestroyView.as_view(), name='gig-update-destroy'),
]