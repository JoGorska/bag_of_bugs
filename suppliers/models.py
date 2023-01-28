from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=220, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name


class PurchaseInvoice(models.Model):
    invoice_number = models.CharField(max_length=220, unique=True, blank=False, null=False)
    date_issued = models.DateField(blank=False, null=False)
    total_net = models.DecimalField(decimal_places=2, max_digits=20, blank=False, null=False)
    VAT_percentage = models.IntegerField(blank=False, null=False)
    suplier = models.ForeignKey(Supplier,  related_name='supplier', on_delete=models.PROTECT, blank=False, null=False)
    delivery_date = models.DateField(blank=False, null=False)
    invoice_due_date = models.DateField(blank=True, null=True)
    paid = models.BooleanField(blank=False, null=False)

    def __str__(self):
        return self.invoice_number
