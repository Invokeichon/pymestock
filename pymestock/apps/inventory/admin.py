from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Item, Inventory

admin.site.register(Item)
admin.site.register(Inventory)