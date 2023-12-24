from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm
from catalog.models import Category, Product, Version


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
        context_data['category_pk'] = category_item.pk
        return context_data


# CreateRUD
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm

    def form_valid(self, form):
        new_product = form.save(commit=False)
        new_product.parent_category_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        # Возвращаем URL списка продуктов для текущей категории
        return reverse('catalog:products_category', kwargs={'pk': self.object.parent_category.pk})

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:products_category', kwargs={'pk': self.object.parent_category.pk})

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, fields=('name', 'version_number', 'version_name', 'is_current'), extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            for form in formset:
                # Устанавливаем родительскую категорию для каждой версии
                form.instance.parent_category = self.object.parent_category
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_category')


# class ProductUpdateView(UpdateView):
#     model = Product
#     form_class = ProductForm
#     # seccess_url = reverse_lazy('catalog:products_category')
#
#     # def get_success_url(self):
#     #     # Возвращаем URL списка продуктов для текущей категории
#     #     return reverse('catalog:products_category', kwargs={'pk': self.object.parent_category.pk})
#
#     def get_context_data(self, **kwargs):
#         context_data = super().get_context_data(**kwargs)
#         VersionFormset = inlineformset_factory(Category, Product, Version, form=VersionForm, extra=1)
#         if self.request.method == 'POST':
#             formset = VersionFormset(self.request.POST, instance=self.object)
#         else:
#             formset = VersionFormset(instance=self.object)
#         context_data['formset'] = formset
#         return context_data
#
#     def form_valid(self, form):
#         context_data = super().get_context_data()
#         formset = context_data['formset']
#         self.object = form.save()
#
#         if formset.is_valid():
#             formset.instance = self.object
#             formset.save()
#         return super().form_valid(form)
#

#
# CRUDelete






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
