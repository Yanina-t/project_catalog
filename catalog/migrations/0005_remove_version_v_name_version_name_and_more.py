# Generated by Django 4.2.5 on 2023-12-24 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_remove_version_name_version_parent_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='version',
            name='v_name',
        ),
        migrations.AddField(
            model_name='version',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='version',
            name='parent_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='version',
            name='version_name',
            field=models.CharField(max_length=100, verbose_name='название версии'),
        ),
        migrations.AlterField(
            model_name='version',
            name='version_number',
            field=models.IntegerField(verbose_name='Номер версии'),
        ),
    ]
