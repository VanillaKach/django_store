from django.core.cache import cache
from .models import Product, Category


def get_products_by_category(category_slug):
    cache_key = f'products_category_{category_slug}'
    products = cache.get(cache_key)

    if not products:
        category = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(
            category=category,
            publish_status='published'
        ).select_related('category', 'owner')

        # Кешируем на 1 час
        cache.set(cache_key, products, 60 * 60)

    return products
