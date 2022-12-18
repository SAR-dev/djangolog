from django.urls import path
from .views import ProfilesCreateView, ProfilesListView, ProfilesRetriveView, ProfilesUpdateDestroyView, SelfProfilesRetriveView

app_name = 'profile'

urlpatterns = [
    path('', ProfilesCreateView.as_view(), name='profile-create'),
    path('list/', ProfilesListView.as_view(), name='profile-list'),
    path('me/', SelfProfilesRetriveView.as_view(), name='profile-list'),
    path('<pk>/', ProfilesRetriveView.as_view(), name='profile-retrive'),
    path('<pk>/update/', ProfilesUpdateDestroyView.as_view(), name='profile-update-destroy'),
]