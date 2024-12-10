# inventory/forms.py
from django import forms
from .models import Inventory

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'quantity']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Inventory.objects.filter(name=name).exists():
            raise forms.ValidationError("An item with this name already exists.")
        return name

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise forms.ValidationError("Quantity must be a positive number.")
        return quantity
