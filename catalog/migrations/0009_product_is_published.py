# Generated by Django 4.2.5 on 2024-01-11 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_product_user_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Признак публикации'),
        ),
    ]