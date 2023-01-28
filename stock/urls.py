from django.urls import path
from views import StockList


urlpatterns = [
    path('', StockList.as_view(), name='stock_list'),

]
