from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.inventory_list, name='inventory_list'),
    path('add-product/', views.add_product, name='add_product'),
    # Add more inventory-related paths here as needed
  
]