from django.db import models


class PurchaseInvoice(models.Model):
    invoice_number = models.CharField()
    date_issued = models.CharField()
    total_net = models.CharField()
    VAT_percentage = models.IntegerField()
    suplier_name = models.CharField()
    delivery_date = models.DateField()

# todo supplier model