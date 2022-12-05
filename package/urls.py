from django.urls import path
from .views import PackageCreateView, PackageListView, PackageRetriveView, PackageUpdateDestroyView

app_name = 'package'

urlpatterns = [
    path('', PackageCreateView.as_view(), name='package-create'),
    path('', PackageListView.as_view(), name='package-list'),
    path('<pk>/', PackageRetriveView.as_view(), name='package-retrive'),
    path('<pk>/', PackageUpdateDestroyView.as_view(), name='package-update-destroy'),
]