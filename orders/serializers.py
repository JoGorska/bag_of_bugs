from rest_framework import serializers
from .models import CustomerOrder, OrderItem
from species.models import Species
from species.serializers import SpeciesSerializer

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

    species_in_stock = Species.objects.filter(stock_item__in_stock=True).distinct()
    species = serializers.PrimaryKeyRelatedField(queryset=species_in_stock)
    # todo I can reuse serializer for species, inherit from serializers.Serializer
    # species = SpeciesSerializer(read_only=True)

    def validate(self, data):
        quantity = data['quantity']
        species = data['species']
        if quantity > species.stock_level:
            raise serializers.ValidationError(
                'Not enough bugs in stock, please reduce quantity'
            )
        return data

    class Meta:
        model = OrderItem
        fields = (
            'order',
            'species',
            'quantity',
            'order_item_total',
        )
        read_only_fields = ('order', 'species')
