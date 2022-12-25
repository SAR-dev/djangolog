from django.urls import path
from .views import OrderCreateView, CreatedOrderListView, OrderDropView, OrderDelayView, RecievedOrderListView, OrderRetriveView, OrderUpdateDestroyView, OrderAcceptView

app_name = 'order'

urlpatterns = [
    path('', OrderCreateView.as_view(), name='order-create'),
    path('created/', CreatedOrderListView.as_view(), name='order-created'),
    path('received/', RecievedOrderListView.as_view(), name='order-received'),
    path('<pk>/', OrderRetriveView.as_view(), name='order-retrive'),
    path('<pk>/update/', OrderUpdateDestroyView.as_view(), name='order-update-destroy'),
    path('<pk>/accept/', OrderAcceptView().as_view(), name='order-accept'),
    path('<pk>/delay/', OrderDelayView().as_view(), name='order-delay'),
    path('<pk>/drop/', OrderDropView().as_view(), name='order-drop'),
]