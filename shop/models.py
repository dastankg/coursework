from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование товара")
    content = models.TextField(blank=True, verbose_name="Информация о товаре")
    img = models.ImageField(upload_to='photos/products/%Y/%m/%d', verbose_name='Фото', blank=True)
    new_price = models.IntegerField(verbose_name="Новая цена")
    old_price = models.IntegerField(verbose_name="Старая цена")
    view_count = models.IntegerField(default=0, verbose_name="Число просмотров")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={'id': self.pk})

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукция'
        ordering = ['-id']


class Review(models.Model):
    post = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="review",
    )
    author = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    comment = models.TextField(max_length=3255)
    title = models.CharField(max_length=15)
