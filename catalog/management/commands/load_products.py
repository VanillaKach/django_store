from django.core.management.base import BaseCommand
from catalog.models import Product, Category
import json

class Command(BaseCommand):
    help = 'Load products from fixtures'

    def handle(self, *args, **options):
        # Удаление старых данных
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Загрузка категорий
        with open('fixtures/categories.json', 'r') as file:
            categories = json.load(file)
            for cat in categories:
                Category.objects.create(
                    name=cat['fields']['name'],
                    description=cat['fields']['description']
                )

        # Загрузка продуктов
        with open('fixtures/products.json', 'r') as file:
            products = json.load(file)
            for prod in products:
                category = Category.objects.get(id=prod['fields']['category'])
                Product.objects.create(
                    name=prod['fields']['name'],
                    description=prod['fields']['description'],
                    category=category,
                    price=prod['fields']['price']
                )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
