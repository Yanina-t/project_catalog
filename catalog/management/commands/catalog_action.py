from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        category_list = [
            {'name': 'Ноутбуки', 'description': 'Компьютеры для мобильного использования'},
            {'name': 'Смартфоны', 'description': 'Мобильные телефоны с различными функциями'},
            {'name': 'Телевизоры', 'description': 'Электроника для домашнего просмотра'},
            {'name': 'Кухонные приборы', 'description': 'Гаджеты для кухни'}
        ]

        # for category_item in category_list:
        #     Category.objects.create(**category_item)

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )
        Category.objects.bulk_create(category_for_create)


        # product_list = [ {'name': 'Dell XPS 13', 'description': 'Мощный и компактный ноутбук', 'purchase_price':
        # 1500}, {'name': 'MacBook Air', 'description': 'Легкий и стильный ноутбук от Apple', 'purchase_price':
        # 290990}, {'name': 'Lenovo ThinkPad X1 Carbon', 'description': 'Производительный бизнес-ноутбук',
        # 'purchase_price': 1600}, {'name': 'iPhone 15 Pro', 'description': 'Последняя модель iPhone',
        # 'purchase_price': 147990}, {'name': 'Samsung Galaxy S21', 'description': 'Мощный Android-смартфон',
        # 'purchase_price': 1000}, {'name': 'Google Pixel 6', 'description': 'Смартфон с отличной камерой',
        # 'purchase_price': 900}, {'name': 'LG OLED C1', 'description': '4K OLED телевизор', 'purchase_price': 2000},
        # {'name': 'Samsung QLED Q80A', 'description': 'QLED-телевизор с технологией Quantum HDR', 'purchase_price':
        # 1800}, {'name': 'Sony BRAVIA XR A90J', 'description': 'Высококачественный телевизор с технологией Acoustic
        # Surface Audio+', 'purchase_price': 2200}, {'name': 'KitchenAid Artisan Stand Mixer', 'description':
        # 'Стойкая миксерная машина', 'purchase_price': 500}, {'name': 'Instant Pot Duo Evo Plus', 'description':
        # 'Многофункциональный мультиварка и медленноварка', 'purchase_price': 150}, {'name': 'Breville Smart Oven
        # Air', 'description': 'Умная духовка с функцией жарки', 'purchase_price': 300}, ]
