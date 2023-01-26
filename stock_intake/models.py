from django.db import models


class PurchaseInvoice(models.Model):
    invoice_number = models.CharField()
    date_issued = models.CharField()
    total_net = models.CharField()
    VAT_percentage = models.IntegerField()
    suplier_name = models.CharField()
    delivery_date = models.DateField()
    invoice_due_date = models.DateField()
    paid = models.BooleanField()

# todo supplier model