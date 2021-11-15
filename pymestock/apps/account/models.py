from django.contrib.auth.models import AbstractUser
from django.db.models.fields import BooleanField, CharField


class User(AbstractUser):
    pyme = CharField(max_length=30)
    is_owner = BooleanField("owner status", default=False)
    is_worker = BooleanField("worker status", default=False)
