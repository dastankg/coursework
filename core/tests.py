from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def test_url_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('homepage'))
        self.assertTemplateUsed(response, 'core/index.html')

    def test_template_content(self):
        response = self.client.get(reverse("homepage"))
        self.assertContains(response, "<h2>Trending Products</h2>")
        self.assertNotContains(response, "Not on the page")
