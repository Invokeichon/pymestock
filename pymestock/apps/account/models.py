from django.contrib.auth.models import AbstractUser
from pymestock.apps.business.models import Business
from django.db import models


class User(AbstractUser):
    business = models.ForeignKey(Business, null=True, on_delete=models.CASCADE)
    is_owner = models.BooleanField("owner status", default=False)
