from django.db import models


class Business(models.Model):
    business_name = models.CharField(max_length=50)
    logo = models.ImageField()
