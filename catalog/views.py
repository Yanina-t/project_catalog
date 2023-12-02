from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Category, Product


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'catalog/contact.html')


def home(request):
    context = {
        'object_list': Product.objects.all()[:4],
        'title': 'Категории'
    }
    return render(request, 'catalog/index_home.html', context)


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории'
    }


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(parent_category=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'Все товары категории {category_item.name}'
        return context_data

# def categories(request):
#     context = {
#         'object_list': Category.objects.all(),
#         'title': 'Категории'
#     }
#     return render(request, 'catalog/category_list.html', context) category_list ранее index_category

# def products_category(request, pk):
#     category_item = Category.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(parent_category=pk),
#         'title': f'Все товары категории {category_item.name}'
#     }
#     return render(request, 'catalog/product_list.html', context) product_list ранее index_prod
