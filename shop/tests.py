from django.test import TestCase

from shop.models import *


class ShopTestCase(TestCase):
    def test_open_shop_success(self):
        url = reverse('shop')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class ShopDetailsTestCase(TestCase):
    def setUp(self):
        self.product1 = Product.objects.create(title='Огурец', content='Самый свежий', new_price=5, old_price=7)

    def test_if_product_is_ogurec(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.title, 'Огурец')
