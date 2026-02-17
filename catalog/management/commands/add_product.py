from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Load test data from fixture'

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Product.objects.filter(id=5).delete()
        Product.objects.filter(id=6).delete()

        category, _ = Category.objects.get_or_create(name='Овощи')

        products = [
            {'name': 'Картофель', 'description': 'Картофель.', 'price': 60, 'image': 'photos/potato.png',
             'category': category},
            {'name': 'Огурец', 'description': 'Огурец.', 'price': 130, 'image': 'photos/cucumber.png',
             'category': category},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully added student: {product.name} {product.category}'))
            else:
                self.stdout.write(
                    self.style.WARNING(f'Product already exists: {product.name} {product.category}'))
