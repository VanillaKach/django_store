from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, TemplateView


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'
    paginate_by = 5

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'


def home(request):
    products = Product.objects.order_by('-created_at')
    paginator = Paginator(products, 5)  # По 5 товаров на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalog/home.html', {'page_obj': page_obj})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'catalog/add_product.html', {'form': form})
