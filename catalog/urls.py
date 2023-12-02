from django.urls import path

from blog.views import blog
from catalog.apps import CatalogConfig
from catalog.views import home, contact, ProductListView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('<int:pk>/catalog/', ProductListView.as_view(), name='products_category'),
]
