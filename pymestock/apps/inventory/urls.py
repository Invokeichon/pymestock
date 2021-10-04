from django.urls import path

from . import views

urlpatterns = [
    path("inventory.html", views.inventory, name="inventory"),
]
