from modeltranslation.translator import register, TranslationOptions

from .models import Feedback


@register(Feedback)
class FeedbackTranslationOptions(TranslationOptions):
    fields = ('first_name', 'title', 'message')
