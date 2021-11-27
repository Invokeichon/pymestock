from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from .models import Item
from pymestock.apps.business.models import Business
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login")
def inventory(request, filter=''):
    items = Item.objects.filter(business=request.user.business.id, name__startswith=filter)

    if request.method == "GET":
        return render(request, "inventory/inventory.html", {"inventory": items})

    if request.method == "POST":
        if "Edit" in request.POST:
            return HttpResponseRedirect(f"/inventory/edit_inventory/{filter}")

        if "Filter" in request.POST:
            new_filter = request.POST["name"]
            return HttpResponseRedirect(f"/inventory/{new_filter}")



@login_required(login_url="/login")
def edit_inventory(request, filter=''):

    if not request.user.is_owner:
        return HttpResponseRedirect(f"/inventory/{filter}")

    items = Item.objects.filter(business=request.user.business.id, name__startswith=filter)

    if request.method == "GET":
        return render(request, "inventory/edit_inventory.html", {"inventory": items})

    if request.method == "POST":

        if "Filter" in request.POST:
            new_filter = request.POST["name"]
            return HttpResponseRedirect(f"/inventory/edit_inventory/{new_filter}")

        if "SaveChanges" in request.POST:
            for item in items:
                stock = request.POST[str(item.id)]
                item.stock_actual = stock
                item.save()

            return HttpResponseRedirect(f"/inventory/{filter}")


@login_required(login_url="/login")
def add_item(request):

    if not request.user.is_owner:
        return HttpResponseRedirect("/dashboard")

    if request.method == "GET":
        return render(request, "inventory/add_item.html")

    if request.method == "POST":
        if "AddItem" in request.POST:
            business = Business.objects.get(id=request.user.business.id)
            name = request.POST["name"]

            brand = request.POST["brand"]
            price = request.POST["price"]
            description = request.POST["description"]

            nuevo_item = Item(business=business, name=name, brand=brand, price=price,
                              description=description, stock_actual=0)
            nuevo_item.save()

            return HttpResponseRedirect("/inventory")
