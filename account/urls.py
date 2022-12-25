from django.urls import path
from .views import MeRetriveView, MeUpdateView, UserRegisterView, ChangePasswordView

app_name = 'account'

urlpatterns = [
	path('create/', UserRegisterView.as_view(), name='create'),
	path('me/', MeRetriveView.as_view(), name='me'),
	path('update/', MeUpdateView.as_view(), name='update'),
	path('change-password/', ChangePasswordView.as_view(), name='update'),
]