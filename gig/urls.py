from django.urls import path
from gig.views import GigCategoryListCreateView, GigRetriveUpdateDestroyView

app_name = 'gig'

urlpatterns = [
    path('', GigCategoryListCreateView.as_view(), name='gig-list-create'),
    path('<pk>/', GigRetriveUpdateDestroyView.as_view(), name='gig-retrive-update-destroy'),
]