from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *


@admin.register(Faq)
class FaqAdmin(TranslationAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description',)


@admin.register(FaqFeedback)
class FaqFeedbackAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'title',
                    'email', 'created_at', 'checked')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'message', 'created_at')
    list_editable = ('checked',)
    list_filter = ('checked', 'created_at')
    fields = ('name', 'email', 'phone', 'title', 'message', 'created_at',
              'checked')
    readonly_fields = ('name', 'email', 'title',
                       'message', 'phone', "created_at")
