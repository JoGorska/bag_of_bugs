from rest_framework import serializers
from .models import CustomerOrder, OrderItem


class CustomerOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerOrder
        fields = (
            'id',
            'reference_code',
            'order_total',
            'delivery_address',
            'postcode',
            'user',
            'date',
        )


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'order',
            'species',
            'quantity',
            'order_item_total',
        )
