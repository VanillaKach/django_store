from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin

# CBV для продуктов
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')

class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = '/users/login/'
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/users/login/'
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/users/login/'
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

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
