# Generated by Django 4.0.4 on 2022-06-16 20:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0006_remove_product_content_en_remove_product_content_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='content_en',
            field=models.TextField(blank=True, null=True, verbose_name='Информация о товаре'),
        ),
        migrations.AddField(
            model_name='product',
            name='content_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Информация о товаре'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Наименование товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Наименование товара'),
        ),
        migrations.AddField(
            model_name='review',
            name='comment_en',
            field=models.TextField(max_length=3255, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='comment_ru',
            field=models.TextField(max_length=3255, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='title_en',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='title_ru',
            field=models.CharField(max_length=15, null=True),
        ),
    ]