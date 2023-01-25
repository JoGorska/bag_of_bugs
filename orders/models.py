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
