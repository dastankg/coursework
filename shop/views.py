from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.generic import ListView

from .models import *


class ShopView(ListView):
    model = Product
    paginate_by = 8
    queryset = Product.objects.all()
    template_name = 'shop/shop.html'
    context_object_name = 'products'

    def get_ordering(self):
        ordering = self.request.GET.get('orderby')
        if ordering == 'Default':
            ordering = '-id'
        elif ordering == 'Popularity':
            ordering = 'view_count'
        elif ordering == 'Price: low to high':
            ordering = 'new_price'
        else:
            ordering = '-new_price'
        return ordering


@cache_page(60)
def product(request, id):
    product = Product.objects.get(id=id)
    product.view_count = product.view_count + 1
    product.save()
    com = product.review.filter(post_id=id)
    feature_products = Product.objects.filter(view_count__lt=10)[:4]
    related_products = Product.objects.all().order_by('view_count')[:4]
    popular_products = Product.objects.filter(view_count__gt=15)[:3]

    if request.method == "POST":
        comment = Review()
        comment.post_id = id
        comment.author = request.POST.get('name')
        comment.email = request.POST.get('email')
        comment.title = request.POST.get('review-title')
        comment.comment = request.POST.get('review-body')
        comment.save()
    return render(request, 'shop/shop-details.html',
                  {'product': product, 'comments': com, 'related_products': related_products,
                   'feature_products': feature_products, 'popular_products': popular_products})
