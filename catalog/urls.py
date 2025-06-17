from django.urls import path
from .views import (
    ProductListView, ProductCreateView,
    ProductUpdateView, ProductDetailView,
    ProductDeleteView, ContactView
)

app_name = 'catalog'

urlpatterns = [
    # Старые URL (FBV) - можно оставить для обратной совместимости
    path('old/', home, name='home_old'),
    path('old/product/<int:pk>/', product_detail, name='product_detail_old'),

    # Новые URL (CBV)
    path('', ProductListView.as_view(), name='product_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', ContactView.as_view(), name='contacts'),
]
