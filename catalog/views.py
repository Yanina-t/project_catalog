from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm
from catalog.models import Category, Product, Version


@login_required
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'catalog/contact.html')


@login_required
def home(request):
    context = {
        'object_list': Product.objects.all()[:4],
        'title': 'Категории'
    }
    return render(request, 'catalog/index_home.html', context)


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    extra_context = {
        'title': 'Категории'
    }


class ProductListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(parent_category=self.kwargs.get('pk'), )
        return queryset

    def get_context_data(self, *args, **kwargs):
        # фильтр кто может видеть созданный продукт
        context_data = super().get_context_data(*args, **kwargs)
        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        # Если пользователь - НЕ модератор, показать только товары, созданные текущим пользователем
        if not self.request.user.is_staff:
            context_data['object_list'] = Product.objects.filter(
                user_product=self.request.user,
                parent_category=category_item
            )

        else:
            # Иначе, показать все товары
            context_data['object_list'] = Product.objects.filter(parent_category=category_item)
        context_data['title'] = f'Все товары категории {category_item.name}'
        context_data['category_pk'] = category_item.pk
        return context_data

    def test_func(self):
        # Этот метод будет вызываться, чтобы проверить условие доступа.
        # В данном случае, пользователь с ролью модератора (is_staff) будет иметь доступ.
        return self.request.user.is_staff or self.request.user


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.save()
        return self.object

    def get_success_url(self):
        return reverse('catalog:products_category', kwargs={'pk': self.object.parent_category.pk})


# CreateRUD
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_product = self.request.user
        self.object.parent_category_id = self.kwargs['pk']
        self.object.save()

        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):
        return reverse('catalog:products_category', kwargs={'pk': self.object.parent_category.pk})


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:category')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm,
                                               fields=('name', 'version_number', 'version_name', 'is_current'), extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

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


class ProductDeleteView(LoginRequiredMixin , DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:category')


@login_required
def published_product(request, pk):
    content_item = get_object_or_404(Product, pk=pk)
    if content_item.is_published:
        content_item.is_published = False
    else:
        content_item.is_published = True

    content_item.save()
    return redirect(reverse('catalog:products_category', kwargs={'pk': content_item.parent_category.pk}))
