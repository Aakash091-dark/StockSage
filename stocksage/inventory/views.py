# inventory/views.py
from django.shortcuts import render, redirect
from .models import Inventory
from .forms import InventoryForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def inventory_list(request):
    items = Inventory.objects.all()  # Replace with your actual queryset
    paginator = Paginator(items, 10)  # 10 items per page

    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)  # If page is not an integer, show first page
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)  # If page is out of range, show last page

    return render(request, 'inventory/inventory_list.html', {'page_obj': page_obj})

# Add Inventory
def add_inventory(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm()
    return render(request, 'inventory/inventory_form.html', {'form': form})

# Edit Inventory
def edit_inventory(request, pk):
    item = Inventory.objects.get(pk=pk)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm(instance=item)
    return render(request, 'inventory/inventory_form.html', {'form': form})

# Delete Inventory
def delete_inventory(request, pk):
    item = Inventory.objects.get(pk=pk)
    item.delete()
    return redirect('inventory_list')




