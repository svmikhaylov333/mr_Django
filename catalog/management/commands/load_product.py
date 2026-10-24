from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.core.management import call_command





class Command(BaseCommand):
    help = 'Удаляет старые данные и загружает тестовые продукты из фикстуры'

    def handle(self, *args, **options):
        # Удаляем старые данные
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Данные удалены"))
        # Загружаем новые
        try:
            call_command('loaddata', 'catalog.json')
            self.stdout.write(self.style.SUCCESS("Данные из файла json загружены"))
        except Exception as exp:
            self.stdout.write(self.style.ERROR(f"ошибка при загрузке: {exp}"))