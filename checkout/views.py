import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from cart.utils.cart import Cart
from .models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    if request.method == 'POST':
        if request.POST.get('radio-group') == 'card':
            order = Order()
            order.first_name = request.POST.get('first')
            order.last_name = request.POST.get('last')
            order.address = request.POST.get('address')
            order.phone = request.POST.get('phone')
            order.notes = request.POST.get('notes')
            order.pay_method = request.POST.get('radio-group')
            order.paid = True
            order.save()

        else:
            order = Order()
            order.first_name = request.POST.get('first')
            order.last_name = request.POST.get('last')
            order.address = request.POST.get('address')
            order.phone = request.POST.get('phone')
            order.notes = request.POST.get('notes')
            order.pay_method = request.POST.get('radio-group')
            order.save()

    return render(request, 'checkout.html')


def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')


def checkout_create_session(request):
    if request.method == 'POST':
        cart = Cart(request)
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],

            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': int(cart.get_total_price()) * 100,
                        'product_data': {
                            'name': 'product_cart'
                        },
                    },
                    'quantity': 1,
                }
            ],
            mode='payment',
            success_url='http://dast4n.pythonanywhere.com/checkout/success/',
            cancel_url='http://dast4n.pythonanywhere.com/checkout/cancel/')
        return JsonResponse({
            'id': checkout_session.id})
