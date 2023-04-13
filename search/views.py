from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
from django.views.decorators.http import require_POST

from blog.models import Post
from shop.models import Product


@require_POST
def search_shop(request):
    query = request.POST.get('search')

    results = Product.objects.filter(Q(title__icontains=query))
    paginator = Paginator(results, 8)
    page = request.GET.get('page')
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
    return render(request, 'search/shop-search.html', {'products': results})


@require_POST
def search_blog(request):
    query = request.POST.get('search')

    results = Post.objects.filter(Q(title__icontains=query))
    paginator = Paginator(results, 6)
    page = request.GET.get('page')
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
    return render(request, 'search/blog-search.html', {'posts': results})
