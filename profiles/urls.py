from django.urls import path
from .views import ProfilesCreateView, ProfilesListView, ProfilesRetrieveView, ProfilesUpdateDestroyView, ProfilesRetrieveByUsernameView

app_name = 'profile'

urlpatterns = [
    path('', ProfilesCreateView.as_view(), name='profile-create'),
    path('list/', ProfilesListView.as_view(), name='profile-list'),
    path('me/', ProfilesRetrieveView.as_view(), name='profile-retrieve'),
    path('me/update/', ProfilesUpdateDestroyView.as_view(), name='profile-update-destroy'),
    path('username/<str:username>/', ProfilesRetrieveByUsernameView.as_view(), name='profile-list'),
]