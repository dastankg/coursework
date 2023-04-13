from django.urls import path

from cart import views

urlpatterns = [
    path('', views.detail, name='cart-detail'),
    path('add/<int:product_id>', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    path('update/<int:product_id>/<int:count>', views.cart_update, name='cart_update'),
]
