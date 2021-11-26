from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Item, Inventory, MeasureUnit
from pymestock.apps.business.models import Business

def inventory(request):
    if request.user.is_authenticated:
        mis_items = Item.objects.filter(business_id=request.user.business.id)
        return render(request, "inventory/inventory.html", {"inventory": mis_items})
    else:
        return HttpResponseRedirect("/login")

def add_item(request):

    if request.method == "GET":
        return render(request, "inventory/add_item.html")

    if request.method == "POST":
        if "AddItem" in request.POST:
            business = Business.objects.get(id=request.user.business.id)
            sku = request.POST["sku"]
            name = request.POST["name"]
            brand = request.POST["brand"]
            price = request.POST["price"]
            description = request.POST["description"]
            category = request.POST["category"]

            if request.user.is_authenticated:
                nuevo_item = Item(business=business, sku=sku, name=name, brand=brand, price=price,
                                  description=description, category=category)
                nuevo_item.save()
                mis_items = Item.objects.filter(business=request.user.business.id)
                return render(request, "inventory/inventory.html", {"inventory": mis_items})
            else:
                return render(request, "account/login.html")
