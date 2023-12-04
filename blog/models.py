from django.db import models
from django.utils.text import slugify


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, unique=True, verbose_name='Slug', default='', blank=True)
    content = models.TextField(verbose_name='Содержимое')
    img_preview = models.ImageField(upload_to='blog_previews/', null=True, blank=True, verbose_name='Превью')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.title}'

    def save(self, *args, **kwargs):
        # Генерация slug на основе заголовка, если он не установлен
        if not self.slug:
            self.slug = slugify(self.title)

        # Переместите вызов родительского метода save внутрь условия
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'


