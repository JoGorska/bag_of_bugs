from django.contrib import admin
from .models import StockItem, ManualStockUpdate, LossGainReason


class StockItemAdmin(admin.ModelAdmin):

    model = StockItem
    list_display = [
        'reference_code',
        'species',
        'invoice',
        'sale_price',
        'order',
        'manual_stock_update',
        'in_stock',
        'updated',
    ]


admin.site.register(StockItem, StockItemAdmin)
admin.site.register(ManualStockUpdate)
admin.site.register(LossGainReason)
