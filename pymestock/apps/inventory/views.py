from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Item
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
            name = request.POST["name"]
            brand = request.POST["brand"]
            price = request.POST["price"]
            description = request.POST["description"]

            if request.user.is_authenticated:
                nuevo_item = Item(business=business, name=name, brand=brand, price=price,
                                  description=description, stock_actual=0)

                nuevo_item.save()

                my_inventory = Item.objects.filter(business=request.user.business.id)

                return render(request, "inventory/inventory.html", {"inventory": my_inventory})
            else:
                return render(request, "account/login.html")


def edit_inventory(request):

    if request.method == "GET" and request.user.is_authenticated:
        my_inventory = Item.objects.filter(business=request.user.business.id)
        return render(request, "inventory/edit_inventory.html", {"inventory": my_inventory})

    if request.method == "POST":
        if "SaveChanges" in request.POST:
            for item in Item.objects.filter(business=request.user.business.id):
                stock = request.POST[str(item.id)]
                item.stock_actual = stock
                item.save()

            my_inventory = Item.objects.filter(business=request.user.business.id)
            return HttpResponseRedirect("/inventory", {"inventory": my_inventory})