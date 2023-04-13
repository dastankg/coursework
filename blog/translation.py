from modeltranslation.translator import register, TranslationOptions

from .models import Post, Comment


@register(Post)
class PostTranslationOption(TranslationOptions):
    fields = ('title', 'posts_text')


@register(Comment)
class CommentTranslationOption(TranslationOptions):
    fields = ('comment',)
