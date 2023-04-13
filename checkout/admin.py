from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Order


@admin.register(Order)
class OrderAdmin(TranslationAdmin):
    list_display = ('first_name', 'last_name', 'address', 'phone', 'notes', 'data', 'paid')
    ordering = ['data']
