from django.test import TestCase, Client
from django.urls import reverse

from shop.models import Product


class CartTestCases(TestCase):

    def setUp(self):
        self.client = Client()
        self.milk = Product.objects.create(title='Milk', content='Milk',
                                           img='photos/products/2022/06/15/top-products-3.jpg', new_price=10,
                                           old_price=15,
                                           view_count=1, time_create='2022-06-15 09:35:04.916403',
                                           time_update='2022-06-15 09:35:04.916471', id=1)

        self.url_add = reverse('cart:cart_add')
        self.url_remove = reverse('cart:cart_remove')
        self.url_detail = reverse('cart:detail')

        self.milk_data = {'product_id': self.milk.id}

    def test_product_is_added(self):
        self.client.post(self.url_add, self.milk_data)
        response = self.client.get(self.url_detail)
        self.assertIn(response, 'Milk')

    def test_product_delete(self):
        self.client.post(self.url_remove, self.milk_data)
        response = self.client.get(self.url_detail)
        self.assertIn(response, 'Milk')
        self.milk.delete()
        response = self.client.get(self.url_detail)
        self.assertNotIn(response, 'Milk')
