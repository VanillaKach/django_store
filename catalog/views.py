from django.shortcuts import render
from catalog.models import Product

def home(request):
    latest_products = Product.objects.order_by('-created_at')[:5]
    return render(request, 'catalog/home.html', {'products': latest_products})
