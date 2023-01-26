import string
import random
from django.db import models


class CustomerOrder(models.Model):
    '''
    customer order has foreign key relation to user
    reverse foreign key relation to StockItems
    once order is placed, the sstock item will become unavailable to
    other customers
    '''
    reference_code = models.CharField()
    user = models.ForeignKey(User)
    date = models.DateField()

    # todo method to get all items from stock items
    def generate_code(self):
        code = ''.join(random.choice(string.ascii_lowercase + string.digits) for character in range(10))
        if CustomerOrder.objects.filter(reference_code=code).exclude(pk=self.pk).exists():
            code = self.generate_code()
        return code