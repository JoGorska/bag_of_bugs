from rest_framework import serializers
from .models import StockItem, ManualStockUpdate


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockItem
        fields = (
            'id',
            'reference_code',
            'species',
            'invoice',
            'net_price',
            'in_stock',
            'updated',

        )


class ManualStockUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ManualStockUpdate
        fields = (
            'reason',
            'incident_raport',
            'stock_affected',
            'confirm_called_police',
            'date_when_called',
            'police_ref',
            'user',
        )
