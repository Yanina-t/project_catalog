from django.shortcuts import render

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

def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории'
    }
    return render(request, 'catalog/index_category.html', context)

def products_category(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(parent_category=pk),
        'title': f'Все товары категории {category_item.name}'
    }
    return render(request, 'catalog/index_prod.html', context)
