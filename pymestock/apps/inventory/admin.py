from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Item, Inventory, MeasureUnit

admin.site.register(Item)
admin.site.register(Inventory)
admin.site.register(MeasureUnit)