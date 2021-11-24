from django.urls import path

from . import views

urlpatterns = [
    path("inventory.html", views.inventory, name="inventory"),
    path("inventory/add_item.html", views.add_item, name="add_item")
]
