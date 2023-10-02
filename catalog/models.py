from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image_preview = models.ImageField(upload_to='product/', verbose_name='Изображение (превью)')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    purchase_price = models.IntegerField(verbose_name='Цена за покупку')
    date_of_creation = models.DateTimeField(verbose_name='Дата создания')
    date_of_last_modification = models.DateTimeField(verbose_name='Дата последнего изменения')

    in_stock = models.BooleanField(default=True, verbose_name='В наличии на складе')


    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} \n {self.description} \n {self.category} \n {self.purchase_price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name} \n {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)
