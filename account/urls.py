from django.urls import path
from .views import MeRetrieveView, MeUpdateView, UserRegisterView, ChangePasswordView

app_name = 'account'

urlpatterns = [
	path('register/', UserRegisterView.as_view(), name='register'),
	path('me/', MeRetrieveView.as_view(), name='me'),
	path('update/', MeUpdateView.as_view(), name='update'),
	path('change-password/', ChangePasswordView.as_view(), name='update'),
]