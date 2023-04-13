from modeltranslation.translator import register, TranslationOptions

from .models import Product, Review


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('comment', 'title')
