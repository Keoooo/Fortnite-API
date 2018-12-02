from django.test import TestCase
from .models import fortniteskins
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient


client = APIClient()
client.get('/api/outfits/13/', format='json')

class ModelTestCase(APITestCase):
    """This class defines the test suite for the bucketlist model."""

    def testGet(self):
        """Define the test client and other test variables."""
        data = {}
        url = "/api/outfits/13/"
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

