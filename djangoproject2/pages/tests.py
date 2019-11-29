from django.test import TestCase
from django.test import SimpleTestCase

# Create your tests here.

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_aboutus_page_status_code(self):
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)

    def test_base_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
