from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    # created_at = models.DateTimeField(**NULLABLE, verbose_name='Создано')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image_preview = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='Изображение (превью)')
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    purchase_price = models.IntegerField(verbose_name='Цена за покупку')
    date_of_creation = models.DateTimeField(**NULLABLE, verbose_name='Дата создания')
    date_of_last_modification = models.DateTimeField(**NULLABLE, verbose_name='Дата последнего изменения')

    # in_stock = models.BooleanField(default=True, verbose_name='В наличии на складе')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} \n {self.description} \n {self.parent_category} \n {self.purchase_price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
