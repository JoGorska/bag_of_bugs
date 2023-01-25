from django.db import models

# Create your models here.
class StockItem(models.Model):
    species = models.ForeignKey()
    invoice = models.ForeignKey()
    net_price = models.DecimalField()
    sale_price = models.DecimalField()

    class Meta:
        ordering = ['invoice__delivery_date']

# todo methods: gross price
# todo methods vat from invoice



class PurchaseInvoice(models.Model):
    invoice_number = models.CharField()
    date_issued = models.CharField()
    total_net = models.CharField()
    VAT_percentage = models.IntegerField()
    suplier_name = models.CharField()
    delivery_date = models.DateField()


class LossGainReason(models.Model):
    name = models.CharField()


class ManualStockUpdate(models.Model):
    stock_item = models.ForeignKey(StockItem)
    reason = models.ForeignKey(LossGainReason)
    date = models.DateTimeField()  # todo date time now
    user = models.ForeignKey()
    confirm_called_police = models.BooleanField()
    date_when_called = models.DateField
    police_ref = models.CharField




