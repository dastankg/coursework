from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from cart.utils.cart import Cart
from shop.models import Product


def detail(request):
    cart = Cart(request)
    return render(request, template_name='cart/detail.html', context={'cart': cart})


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    cart.add(product=product)
    return redirect('cart-detail')


def cart_update(request, product_id, count):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    cart.update(product=product, count=count)
    return redirect('cart-detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart-detail')
