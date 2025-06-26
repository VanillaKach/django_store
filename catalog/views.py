import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy
from blog import models
from .models import Product, Category
from .forms import ProductForm
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import permission_required
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .services import get_products_by_category
from django.core.cache import cache

# CBV для продуктов
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    paginate_by = 10
    context_object_name = 'products'

    def get_queryset(self):
        cache_key = 'product_list_all'
        products = cache.get(cache_key)

        if not products:
            products = super().get_queryset()
            # Кешируем QuerySet
            cache.set(cache_key, products, 60 * 30)  # 30 минут

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cache_timestamp'] = cache.get('product_list_timestamp')
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = '/users/login/'
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = '/users/login/'
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        product = self.get_object()
        # Владелец или модератор
        return (product.owner == self.request.user or
                self.request.user.has_perm('catalog.can_change_publish_status'))

    def handle_no_permission(self):
        raise PermissionDenied("У вас нет прав для редактирования этого продукта")


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = '/users/login/'
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

    def test_func(self):
        product = self.get_object()
        # Владелец или модератор
        return (product.owner == self.request.user or
                self.request.user.has_perm('catalog.delete_product'))

    def handle_no_permission(self):
        raise PermissionDenied("У вас нет прав для удаления этого продукта")


# Другие представления
class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'

# Старые FBV (можно оставить для обратной совместимости)
def home(request):
    products = Product.objects.order_by('-created_at')
    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalog/home.html', {'page_obj': page_obj})

def product_detail_old(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail_old.html', {'product': product})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:product_list')
    else:
        form = ProductForm()
    return render(request, 'catalog/add_product.html', {'form': form})


@permission_required('catalog.can_change_publish_status')
def change_publish_status(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Product.PUBLISH_STATUS):
            product.publish_status = new_status
            product.save()
    return redirect('catalog:product_detail', pk=product.pk)


@method_decorator(cache_page(60 * 5), name='dispatch')  # Кешируем на 5 минут
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now()  # Для проверки работы кеша
        return context


class CategoryProductsView(ListView):
    template_name = 'catalog/category_products.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return get_products_by_category(self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
