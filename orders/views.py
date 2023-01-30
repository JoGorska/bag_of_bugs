from rest_framework import generics
from .models import CustomerOrder, OrderItem
from .serializers import OrderItemSerializer, CustomerOrderSerializer


class OrdersList(generics.ListCreateAPIView):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer
    depth = 1


class OrderItemsList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    lookup_field = 'order__reference_code'
    serializer_class = OrderItemSerializer
    depth = 1
