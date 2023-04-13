from django.db import models


# Create your models here.


class Faq(models.Model):
    '''Часто задаваемые вопросы'''
    title = models.CharField('Title', max_length=155)
    description = models.TextField('Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Часто задаваемые вопросы'
        verbose_name_plural = 'Часто задаваемый вопрос'


class FaqFeedback(models.Model):
    '''Часто задаваемые вопросы Зона контактов'''
    name = models.CharField('Name', max_length=155)
    email = models.EmailField('Email',
                              max_length=155, blank=True, null=True)
    phone = models.CharField('Phone', max_length=10)
    title = models.CharField('Subject', max_length=155)
    message = models.TextField('Message')

    checked = models.BooleanField('Checked', default=False)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос к нам'
        verbose_name_plural = 'Вопросы к нам'
