from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy
from blog import models
from .models import Product
from .forms import ProductForm
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import permission_required

# CBV для продуктов
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            return qs.filter(publish_status='published')

        # Для авторизованных пользователей показываем больше
        if self.request.user.has_perm('catalog.can_change_publish_status'):
            return qs
        elif self.request.user.is_authenticated:
            return qs.filter(
                models.Q(publish_status='published') |
                models.Q(owner=self.request.user)
            )
        return qs.filter(publish_status='published')


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = '/users/login/'
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.publish_status = 'moderation'
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
