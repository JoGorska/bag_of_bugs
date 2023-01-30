from django.contrib import admin
from .models import PurchaseInvoice, Supplier


admin.site.register(PurchaseInvoice)
admin.site.register(Supplier)
