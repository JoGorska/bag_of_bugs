from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import CustomerOrder, OrderItem
from .serializers import OrderItemSerializer, CustomerOrderSerializer


class OrdersList(generics.ListCreateAPIView):
    '''
    user needs to create order first, than order items
    '''
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer
    depth = 1


class OrderItemsList(generics.ListCreateAPIView):
    '''
    lists all items within order, on order item save
    the order sum gets saved using signals
    '''
    lookup_field = 'order__reference_code'
    serializer_class = OrderItemSerializer
    depth = 1

    def get_queryset(self):
        code = self.kwargs['reference_code']
        return OrderItem.objects.filter(order__reference_code=code)

    def perform_create(self, serializer):
        code = self.kwargs['reference_code']
        order_instance = get_object_or_404(CustomerOrder, reference_code=code)
        serializer.save(order=order_instance)
