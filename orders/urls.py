from django.urls import path
from .views import OrdersList, OrderItemsList


urlpatterns = [
    path('', OrdersList.as_view(), name='orders_list'),
    path('<str:reference_code>/', OrderItemsList.as_view(), name='order_items_list'),

]