from django.urls import path

from .views import checkout, cancel, success, checkout_create_session

urlpatterns = [
    path('', checkout, name="checkout"),
    path('cancel/', cancel, name='cancel'),
    path('success/', success, name='success'),
    path('create-checkout-session/', checkout_create_session, name='create-checkout-session'),
]
