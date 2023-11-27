from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contact, products_category, categories

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('category/', categories, name='product'),
    path('<int:pk>/catalog/', products_category, name='products_category'),
]
