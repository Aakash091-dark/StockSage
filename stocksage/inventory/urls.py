# inventory/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),  # Default path for inventory list
    path('add/', views.add_inventory, name='add_inventory'),
    path('edit/<int:pk>/', views.edit_inventory, name='edit_inventory'),
    path('delete/<int:pk>/', views.delete_inventory, name='delete_inventory'),
]
