from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from species.models import Species
from suppliers.models import PurchaseInvoice


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
        return f'{self.name}: {self.loss_or_gain}'


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
    updated = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    in_stock = models.BooleanField(blank=False, null=False, default=True)

    def __str__(self):
        return self.reference_code

    class Meta:
        ordering = ['invoice__delivery_date']


class ManualStockUpdate(models.Model):
    '''
    Manual Stock Update happens when loss or gain of stock needs to be recorded,
    all events that affect stock level should be recorded to keep track of the stock
    the normal stock intake would come from purchase invoice
    normal stock outgoing would come from order
    manual stock update is a third option that isn't covered by above situations
    '''
    reference_code = AutoSlugField(populate_from=['reason__name', 'date'], unique=True, blank=False, null=False)
    reason = models.ForeignKey(LossGainReason, related_name='manual_stock_update', on_delete=models.PROTECT, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    user = models.ForeignKey(User, related_name='manual_stock_update', on_delete=models.PROTECT, blank=False, null=False)
    confirm_called_police = models.BooleanField(
        'Confirm, called police: for dangerous species it is obligatory to report incident to Police',
        blank=True, null=True)
    date_when_called = models.DateField(blank=True, null=True)
    police_ref = models.CharField(max_length=220, blank=True, null=True)
    incident_raport = models.TextField(blank=True, null=True)
    stock_affected = models.ManyToManyField(StockItem, related_name='manual_update', blank=True)

    def __str__(self):
        return self.reference_code

    class Meta:
        ordering = ['date']


@receiver(m2m_changed, sender=ManualStockUpdate.stock_affected.through)
def update_in_stock_status(sender, instance, **kwargs):
    '''
    captures many to many field changed signal and saves each stock item
    that was affected by the incident to in stock true or false
    '''
    action = kwargs.pop('action', None)
    if action == 'post_add':
        stock_update_object = instance
        stock_items = stock_update_object.stock_affected.all()
        for item in stock_items:
            if stock_update_object.reason.loss_or_gain == LossGainReason.LOSS:
                item.in_stock = False
                item.save()
            else:
                item.in_stock = True
                item.save()
