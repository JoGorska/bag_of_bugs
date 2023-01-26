from django.db import models


class Species(models.Model):
    name = models.CharField(max_length=220, unique=True, blank=False, null=False)
    latin_name = models.CharField(max_length=220, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    dangerous_species = models.BooleanField(blank=False, null=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=220, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=220, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name


class EnviromentRequirements(models.Model):
    name = models.CharField(max_length=220, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name
