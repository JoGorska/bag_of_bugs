from rest_framework import serializers
from .models import CustomerOrder, OrderItem


class CustomerOrderSerializer(serializers.ModelSerializer):
    reference_code = serializers.ReadOnlyField()
    order_total = serializers.ReadOnlyField()

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
    # enviroment = serializers.PrimaryKeyRelatedField(queryset=Enviroment.objects.all())
    # todo - need to capture value of key from url to get the order
    # todo need to return error if quantity exceeds stock
    class Meta:
        model = OrderItem
        fields = (
            'order',
            'species',
            'quantity',
            'order_item_total',
        )
