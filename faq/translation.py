from modeltranslation.translator import register, TranslationOptions

from .models import Faq, FaqFeedback


@register(Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(FaqFeedback)
class FaqFeedbackTranslationOptions(TranslationOptions):
    fields = ('title', 'message')
