from django.db import models


# Create your models here.
class Species(models.Model):
    name = models.CharField()
    latin_name = models.CharField()
    description = models.CharField()
    dangerous_species = models.BooleanField()


class Category(models.Model):
    name = models.CharField()


class Size(models.Model):
    name = models.CharField()


class EnviromentRequirements(models.Model):
    name = models.CharField()
