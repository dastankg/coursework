from django.db import models


class Feedback(models.Model):
    '''Форма обратной связи'''
    first_name = models.CharField('First Name', max_length=155)
    last_name = models.CharField('Last Name', max_length=155)
    email = models.EmailField('Your Email', max_length=155)
    phone = models.IntegerField('Your Phone')
    title = models.CharField('Your Subject', max_length=155)
    message = models.TextField('Your Message')

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Date')

    def __str__(self):
        return self.message[:20]

    class Meta:
        verbose_name = 'Форма обратной связь'
        verbose_name_plural = 'Формы обратной связи'


class Subscribe(models.Model):
    '''Подписка по email'''
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Подписка по email'
        verbose_name_plural = 'Подписки по email'
