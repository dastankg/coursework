from django.urls import path

from .views import search_blog, search_shop

urlpatterns = [
    path('products/', search_shop, name='search_shop'),
    path('posts/', search_blog, name='search_blog'),
]
