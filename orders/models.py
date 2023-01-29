import uuid
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.db.models import Sum
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
from species.models import Species


class CustomerOrder(models.Model):
    '''
    customer order has foreign key relation to user
    reverse foreign key relation to StockItems
    once order is placed, the sstock item will become unavailable to
    other customers
    '''
    reference_code = models.CharField(max_length=10, unique=True, blank=False, null=False)
    user = models.ForeignKey(User, related_name='customer_order', on_delete=models.PROTECT, blank=False, null=False)
    date = models.DateField(auto_now_add=True, blank=False, null=False)
    delivery_address = models.CharField(max_length=220, unique=True, blank=False, null=False)
    # postcode validator regex from https://stackoverflow.com/questions/164979/regex-for-matching-uk-postcodes
    # example CM23 3DH
    postcode = models.CharField(
        validators=[
            RegexValidator(
                regex='([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})',
                message='Please enter valid UK postcode'
            )],
        max_length=20, null=True, blank=True
    )
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(
                        Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def generate_code(self):
        code = uuid.uuid4().hex.upper()
        if CustomerOrder.objects.filter(reference_code=code).exclude(pk=self.pk).exists():
            code = self.generate_code()
        return code

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.reference_code:
            self.reference_code = self.generate_code()

    def __str__(self):
        return self.reference_code


class OrderItem(models.Model):
    '''
    list of items with quantities that were ordered
    assuming customer buys particular species, not stock items
    stock items are decreased seperately
    '''
    order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE, related_name="order_tems", null=False, blank=False)
    species = models.ForeignKey(Species, on_delete=models.PROTECT, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    order_item_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.order_item_total = self.species.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Slug {self.species.slug} on order {self.order.reference_code}'


@receiver(post_save, sender=OrderItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    handles signals from post save event
    to update total within order item
    """
    instance.order.update_total()
