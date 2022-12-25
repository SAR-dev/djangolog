from django.shortcuts import render
from .models import Order
from .serializers import OrderWriteSerializer, OrderReadSerializer
from rest_framework import generics, views, response, permissions, exceptions, status
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist
from django_filters import rest_framework as filters
from utils.paginations import PazeSizePagination
from django.db.models import Q

class IsOrderAuthor(permissions.BasePermission):
    message = "You can not view this route!"

    def has_permission(self, request, view):
        try:
            order = Order.objects.get(pk=view.kwargs.get("pk"))
            author = gig.buyer == request.user
            return author
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)


class OrderCreateView(generics.CreateAPIView):
    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)

    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderWriteSerializer


class CreatedOrderListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderReadSerializer
    
    def get_queryset(self):
        try:
            return Order.objects.filter(buyer__id=self.request.user.id)
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)

class RecievedOrderListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderReadSerializer

    def get_queryset(self):
        try:
            return Order.objects.filter(package__author__id=self.request.user.id)
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)

class OrderRetriveView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderReadSerializer

class OrderUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOrderAuthor]
    queryset = Order.objects.all()
    serializer_class = OrderWriteSerializer

class OrderAcceptView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            order = Order.objects.get(id=pk)
            if request.user.id == order.package.author.id:
                order.status = "accepted"
                order.save()
            return response.Response({
                'accepted': True
            })
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)

        try:
            order = Order.objects.get(id=pk)
            if request.user.id == order.package.author.id:
                order.status = "cancelled"
                order.save()
            return response.Response({
                'cancelled': True
            })
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)
