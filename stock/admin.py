from django.contrib import admin
from .models import StockItem, ManualStockUpdate, LossGainReason


class StockItemAdmin(admin.ModelAdmin):

    model = StockItem
    list_display = [
        'reference_code',
        'species',
        'invoice',
        'updated',
        'in_stock'
    ]


admin.site.register(StockItem, StockItemAdmin)
admin.site.register(ManualStockUpdate)
admin.site.register(LossGainReason)
