from django.db import models
from django_extensions.db.fields import AutoSlugField


class Category(models.Model):
    '''
    for example: spider, ant, fly
    '''
    name = models.CharField(max_length=220, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Size(models.Model):
    '''
    for example: small, medium, large
    '''
    name = models.CharField(max_length=220, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name


class Enviroment(models.Model):
    '''
    for example: indoor, outdoor
    '''
    name = models.CharField(max_length=220, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name


class Species(models.Model):
    '''
    model describing bugs that can be sold in the shop
    '''
    name = models.CharField(max_length=220, unique=True, blank=False, null=False)
    slug = AutoSlugField(populate_from=['name'], unique=True, blank=False, null=False)
    latin_name = models.CharField(max_length=220, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    dangerous_species = models.BooleanField(blank=False, null=False)
    category = models.ForeignKey(Category, related_name='species', on_delete=models.PROTECT, blank=False, null=False)
    size = models.ForeignKey(Size, related_name='species', on_delete=models.PROTECT, blank=False, null=False)
    enviroment = models.ForeignKey(Enviroment, related_name='species', on_delete=models.PROTECT, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "species"

    @property
    def stock_level(self):
        '''
        reverse foreign key lookup
        '''
        return self.stock_item.filter(in_stock=True).count()
