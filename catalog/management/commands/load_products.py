from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Load initial data for products and categories'

    def handle(self, *args, **options):
        self.stdout.write("Deleting old data...")
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write("Loading fixtures...")
        call_command('loaddata', 'categories.json', app_label='catalog')
        call_command('loaddata', 'products.json', app_label='catalog')

        self.stdout.write(self.style.SUCCESS('Successfully loaded data'))
