import string
import random
from django.db import models
from django.contrib.auth.models import User


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

    # todo method to get all items from stock items
    def generate_code(self):
        code = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
        if CustomerOrder.objects.filter(reference_code=code).exclude(pk=self.pk).exists():
            code = self.generate_code()
        return code

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.reference_code:
            self.reference_code = self.generate_code()

    def __str__(self):
        return self.reference_code
