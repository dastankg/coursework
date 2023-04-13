from django.shortcuts import render
from django.views.decorators.cache import cache_page

from blog.models import Post
from shop.models import Product


@cache_page(60)
def homepage(request):
    product = Product.objects.all().order_by('id')
    trending_products = Product.objects.filter(view_count__gt=10)[:8]
    featured_products = Product.objects.filter(view_count__lt=10)[:8]
    best_seller_products = Product.objects.filter(new_price__lt=4)
    latest_blog = Post.objects.order_by('-pk')[:3]

    return render(request, 'core/index.html', {'product': product, 'trending_products': trending_products, \
                                               'featured_products': featured_products,
                                               'best_seller_products': best_seller_products,
                                               'latest_blog': latest_blog})


def terms_conditions(request):
    return render(request, 'core/terms-of-service.html')


def pravicy_policy(request):
    return render(request, 'core/pravicy-policy.html')
