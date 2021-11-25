from django.shortcuts import render
from .models import Item, Inventory, MeasureUnit
from pymestock.apps.business.models import Business

def inventory(request):
    if request.user.is_authenticated:
        mis_items = Item.objects.filter(id_business = Business.objects.filter(owner = request.user))
        return render(request, "inventory/inventory.html", {"inventory": mis_items})
    else:
        return render(request, "account/login.html")

def add_item(request):

    if request.method == "GET":
        return render(request, "inventory/add_item.html")

    if request.method == "POST":
        if "Agregar item" in request.POST:
            id_business = Business.objects.filter(owner = request.user)
            name = request.POST["name"]
            brand = request.POST["brand"]
            price = request.POST["price"]
            description = request.POST["description"]
            category = request.POST["category"]

            if request.user.is_authenticated:
                nuevo_item = Item(id_business=id_business, name=name, brand=brand, price=price,
                                  description=description, category=category)
                nuevo_item.save()
                mis_items = Item.objects.filter(id_business = Business.objects.filter(owner = request.user))
                return render(request, "inventory/inventory.html", {"inventory": mis_items})
            else:
                return render(request, "account/login.html")
