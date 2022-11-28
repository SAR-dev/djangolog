from django.urls import path
from .views import MeRetriveView, MeAvatarUpdateView, UserRegisterView

app_name = 'account'

urlpatterns = [
	path('create/', UserRegisterView.as_view(), name='create'),
	path('me/', MeRetriveView.as_view(), name='me'),
	path('avatar/', MeAvatarUpdateView.as_view(), name='avatar'),
]