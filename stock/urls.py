from django.urls import path
from .views import StockList, ManualStockUpdateList


urlpatterns = [
    path('', StockList.as_view(), name='stock_list'),
    path('stock_update/', ManualStockUpdateList.as_view(), name='manual_stock_update_list'),
]
