from modeltranslation.translator import register, TranslationOptions

from .models import Order


@register(Order)
class OrderTranslationOptions(TranslationOptions):
    fields = ('notes',)
