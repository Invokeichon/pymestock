from django.db import models
from pymestock.apps.business.models import Business


CharField_max_length = 100


class Item(models.Model):
    business = models.ForeignKey(Business, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=CharField_max_length)
    brand = models.CharField(max_length=CharField_max_length)
    price = models.IntegerField()
    description = models.CharField(max_length=CharField_max_length)
    stock_actual = models.IntegerField(null=True)
