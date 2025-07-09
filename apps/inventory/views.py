from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def inventory_list(request):
    return render(request, 'inventory/templates/product_list.html')

def add_product(request):
    # Logic to add a product
    return render(request, 'inventory/templates/add_product.html')



# Add @login_required to all views here when implemented
