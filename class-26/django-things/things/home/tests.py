from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse

class ThingsTests(SimpleTestCase):
    def test_home_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "home.html")
        self.assertTemplateUsed(response, "_base.html")

