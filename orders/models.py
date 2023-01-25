from django.db import models
from stock.models import StockItem
# Create your models here.


class CustomerOrder(models.Model):
    reference_code = models.CharField()
    user = models.ForeignKey()
    date = models.DateField()
    items = models.ManyToManyField(StockItem)
