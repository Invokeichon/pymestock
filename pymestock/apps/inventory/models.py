from django.db import models
from pymestock.apps.business.models import Business


CharField_max_length = 100


class Item(models.Model):
    id_item = models.IntegerField()
    id_business = models.ForeignKey(Business, on_delete=models.CASCADE)
    name = models.CharField(max_length=CharField_max_length)
    brand = models.CharField(max_length=CharField_max_length)
    price = models.IntegerField()
    description = models.CharField(max_length=CharField_max_length)
    category = models.CharField(max_length=CharField_max_length)
    photo = models.ImageField()


class Inventory(models.Model):
    id_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    stock_actual = models.IntegerField()


class MeasureUnit(models.Model):
    category = models.CharField(max_length=CharField_max_length)
    name = models.CharField(max_length=CharField_max_length)
    abbreviation = models.CharField(max_length=CharField_max_length)
