from django.urls import path
from .views import ProfilesCreateView, FollowView, ProfilesListView, ProfilesRetriveView, ProfilesUpdateDestroyView, ProfilesRetriveByUsernameView

app_name = 'profile'

urlpatterns = [
    path('', ProfilesCreateView.as_view(), name='profile-create'),
    path('list/', ProfilesListView.as_view(), name='profile-list'),
    path('username/<str:username>/', ProfilesRetriveByUsernameView.as_view(), name='profile-list'),
    path('follow/<str:username>/', FollowView.as_view(), name='follow'),
    path('<pk>/', ProfilesRetriveView.as_view(), name='profile-retrive'),
    path('<pk>/update/', ProfilesUpdateDestroyView.as_view(), name='profile-update-destroy'),
]