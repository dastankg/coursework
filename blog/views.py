from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from .models import Post, Comment


@cache_page(60)
def blog(request):
    posts = Post.objects.all().order_by('id')
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/blog.html', {'posts': posts})


@cache_page(60)
def post(request, id):
    post = Post.objects.get(id=id)
    post.visit_count = post.visit_count + 1
    post.save()

    pop_posts = Post.objects.all().order_by('visit_count')[:6]
    com = post.comments.filter(post_id=id)

    if request.method == "POST":
        comment = Comment()
        comment.post_id = id
        comment.author = request.POST.get('author')
        comment.email = request.POST.get('email')
        comment.comment = request.POST.get('comment')
        comment.save()

    return render(request, 'blog/blog-details.html', {'post': post, 'comments': com, 'pop_posts': pop_posts})
