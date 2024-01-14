from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contact, ProductListView, CategoryListView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductDetailView, published_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('<int:pk>/catalog/', ProductListView.as_view(), name='products_category'),
    path('<int:pk>/catalog/create/', ProductCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/detail/', ProductDetailView.as_view(), name='product_view'),
    path('catalog/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('published/<int:pk>/', published_product, name='published_product'),
]


# <div class="card-body">
#                     {% csrf_token %}
#                     {{ form.as_p }}
#                     <button type="submit" class="btn btn-success">
#                         {% if object %}
#                         Сохранить
#                         {% else %}
#                         Создать
#                         {% endif %}
#                     </button>
#                     <a href="{% url 'catalog:products_category' object.parent_category.pk%}" type="button" class="btn btn-outline-secondary">Отмена</a>
#                 </div>