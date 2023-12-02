from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, blog, BlogDetailView, BlogUpdateView, BlogDeleteView, published_content

app_name = BlogConfig.name

urlpatterns = [
    path('', blog, name='blog'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('published/<int:pk>/', published_content, name='published_content'),

]
