from django.urls import path

from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('pravicy-policy/', pravicy_policy, name='pravicy_policy'),
    path('terms-of-service/', terms_conditions, name='terms_of_service'),
]
