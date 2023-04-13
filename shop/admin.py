from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from .models import Product


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('title', 'content', 'get_html_img')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_filter = ('time_create',)
    fields = (
        'title', 'content', 'img', 'get_html_img', 'new_price', 'old_price', 'view_count', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_img')

    def get_html_img(self, object):
        if object.img:
            return mark_safe(f"<img src='{object.img.url}' width=50")

    get_html_img.short_description = 'Миниатюра'


admin.site.site_title = 'Админ-панель онлайн магазина Orgo'
admin.site.site_header = 'Админ-панель онлайн магазина Orgo'
