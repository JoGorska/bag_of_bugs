from django.contrib import admin
from .models import OrderItem, CustomerOrder


admin.site.register(OrderItem)
admin.site.register(CustomerOrder)