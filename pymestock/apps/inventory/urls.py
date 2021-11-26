from django.urls import path

from . import views

urlpatterns = [
    path("inventory", views.inventory, name="inventory"),
    path("inventory/add_item", views.add_item, name="add_item"),
    path("inventory/edit_inventory", views.edit_inventory, name="edit_inventory"),
]
