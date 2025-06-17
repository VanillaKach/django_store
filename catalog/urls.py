from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView, ContactView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactView.as_view(), name='contacts'),
]
