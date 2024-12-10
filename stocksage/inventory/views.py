# inventory/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Inventory
from .forms import InventoryForm


# Inventory List
def inventory_list(request):
    search_query = request.GET.get("search", "")
    if search_query:
        inventory_items = Inventory.objects.filter(name__icontains=search_query)
    else:
        inventory_items = Inventory.objects.all()
    return render(
        request,
        "inventory/inventory_list.html",
        {"inventory_items": inventory_items, "search_query": search_query},
    )


# Add Inventory Item
def add_inventory(request):
    if request.method == "POST":
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inventory_list")
    else:
        form = InventoryForm()
    return render(request, "inventory/add_inventory.html", {"form": form})


# Edit Inventory Item
def edit_inventory(request, pk):
    item = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        form = InventoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("inventory_list")
    else:
        form = InventoryForm(instance=item)
    return render(
        request, "inventory/edit_inventory.html", {"form": form, "item": item}
    )


# Delete Inventory Item
def delete_inventory(request, pk):
    item = get_object_or_404(Inventory, pk=pk)
    item.delete()
    return redirect("inventory_list")
