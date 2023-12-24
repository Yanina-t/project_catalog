from django.contrib import admin

from catalog.models import Product, Category, Version


# admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'purchase_price', 'parent_category',)
    list_filter = ('parent_category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('name', 'description',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'version_number', 'is_current')
    search_fields = ('name', 'version_number',)