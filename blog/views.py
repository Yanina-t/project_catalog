from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView, TemplateView
from pytils.translit import slugify

from blog.models import Blog


# Create your views here.
def blog(request):
    context = {
        'object_list': Blog.objects.all(),
    }
    return render(request, 'blog/blog_list.html', context)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


# CreateRUD
class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'img_preview',)
    success_url = reverse_lazy('blog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        # Дополнительные действия после успешного сохранения формы
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'img_preview',)
    success_url = reverse_lazy('blog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        # Дополнительные действия после успешного сохранения формы
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


# CRUDelete
class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog')


def published_content(request, pk):
    content_item = get_object_or_404(Blog, pk=pk)
    if content_item.is_published:
        content_item.is_published = False
    else:
        content_item.is_published = True

    content_item.save()
    return redirect(reverse('blog:blog'))

#
# class DashboardView(TemplateView):
#     template_name = 'dashboard.html'  # Шаблоны
#
