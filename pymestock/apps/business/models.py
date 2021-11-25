from django.db import models
from pymestock.apps.account.models import User


class Business(models.Model):
    business_name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
