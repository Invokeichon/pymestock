from django.shortcuts import render


def inventory(request):
    return render(request, "inventory/inventory.html", {})

def add_item(request):
    return render(request, "inventory/add_item.html", {})
