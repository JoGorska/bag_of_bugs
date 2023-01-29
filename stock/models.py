from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from species.models import Species
from suppliers.models import PurchaseInvoice
from orders.models import CustomerOrder


class LossGainReason(models.Model):
    LOSS = 'loss'
    GAIN = 'gain'

    LOSS_OR_GAINCHOICES = [
        (LOSS, 'loss'),
        (GAIN, 'gain'),
    ]
    name = models.CharField(max_length=220, unique=True, blank=False, null=False)
    loss_or_gain = models.CharField(max_length=220, choices=LOSS_OR_GAINCHOICES, blank=False, null=False, default=LOSS)

    def __str__(self):
        return self.name


class ManualStockUpdate(models.Model):
    reference_code = AutoSlugField(populate_from=['reason__name', 'date'], unique=True, blank=False, null=False)
    reason = models.ForeignKey(LossGainReason, related_name='manual_stock_update', on_delete=models.PROTECT, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    user = models.ForeignKey(User, related_name='manual_stock_update', on_delete=models.PROTECT, blank=False, null=False)
    confirm_called_police = models.BooleanField(blank=True, null=True)
    date_when_called = models.DateField(blank=True, null=True)
    police_ref = models.CharField(max_length=220, blank=True, null=True)
    incident_raport = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.reference_code


class StockItem(models.Model):
    '''
    invoice can add stock items
    order can remove stock item
    manual_stock_update can increase or decrease stock, depending on circumstances
    '''
    reference_code = AutoSlugField(populate_from=['species__name'], unique=True, blank=False, null=False)
    species = models.ForeignKey(Species, related_name='stock_item', on_delete=models.PROTECT, blank=False, null=False)
    invoice = models.ForeignKey(PurchaseInvoice, related_name='stock_item', on_delete=models.PROTECT, blank=True, null=True)
    net_price = models.DecimalField(decimal_places=2, max_digits=20, blank=False, null=False)
    sale_price = models.DecimalField(decimal_places=2, max_digits=20, blank=False, null=False)
    order = models.ForeignKey(CustomerOrder, related_name='stock_item', on_delete=models.PROTECT, blank=True, null=True)
    manual_stock_update = models.ForeignKey(ManualStockUpdate, related_name='stock_item', on_delete=models.PROTECT, blank=True, null=True)
    in_stock = models.BooleanField(blank=False, null=False, default=False)
    updated = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return self.reference_code

    class Meta:
        ordering = ['invoice__delivery_date']

