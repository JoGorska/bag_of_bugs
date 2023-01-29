from rest_framework import generics

from .models import StockItem, ManualStockUpdate
from .serializers import StockSerializer, ManualStockUpdateSerializer


class StockList(generics.ListCreateAPIView):
    queryset = StockItem.objects.all()
    serializer_class = StockSerializer
    depth = 1


class ManualStockUpdateList(generics.ListCreateAPIView):
    queryset = ManualStockUpdate.objects.all()
    serializer_class = ManualStockUpdateSerializer
    depth = 1
