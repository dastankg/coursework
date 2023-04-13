from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from .models import Post


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ('title', 'posts_text', 'posted', 'get_html_img')
    list_display_links = ('title', 'posted')
    search_fields = ('title', 'posts_text')
    fields = ('title', 'posts_text', 'posted', 'img', 'get_html_img', 'visit_count')
    readonly_fields = ('posted', 'get_html_img',)

    def get_html_img(self, object):
        if object.img:
            return mark_safe(f"<img src='{object.img.url}' width=50")

    get_html_img.short_description = 'Миниатюра'
