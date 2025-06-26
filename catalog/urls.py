from django.urls import path
from .views import (
    ProductListView, ProductCreateView,
    ProductUpdateView, ProductDetailView,
    ProductDeleteView, CategoryProductsView,
)

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/<slug:slug>/', CategoryProductsView.as_view(), name='category_products'),
]
