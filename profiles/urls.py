from django.urls import path
from .views import ProfilesCreateView, ProfilesListView, ProfilesRetriveView, ProfilesUpdateDestroyView, ProfilesRetriveByUsernameView

app_name = 'profile'

urlpatterns = [
    path('', ProfilesCreateView.as_view(), name='profile-create'),
    path('list/', ProfilesListView.as_view(), name='profile-list'),
    path('username/<str:username>/', ProfilesRetriveByUsernameView.as_view(), name='profile-list'),
    path('me/', ProfilesRetriveView.as_view(), name='profile-retrive'),
    path('me/update/', ProfilesUpdateDestroyView.as_view(), name='profile-update-destroy'),
]