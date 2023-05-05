from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Company

class CompanyTests(APITestCase):
    def setUp(self):
        self.company1 = Company.objects.create(name='Apple', address='USA')
        self.company2 = Company.objects.create(name='REPLIQ', address='Dhaka')
        self.valid_payload = {'name': 'GP', 'address': 'Dhaka'}
        self.invalid_payload = {'name': '', 'address': 'Invalid Address'}

    def test_get_all_companies(self):
        url = reverse('company-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_valid_company(self):
        url = reverse('company-list')
        response = self.client.post(url, data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'GP')

    def test_create_invalid_company(self):
        url = reverse('company-list')
        response = self.client.post(url, data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_valid_company(self):
        url = reverse('company-detail', kwargs={'pk': self.company1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Apple')

    def test_get_invalid_company(self):
        url = reverse('company-detail', kwargs={'pk': 999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_valid_company(self):
        url = reverse('company-detail', kwargs={'pk': self.company1.id})
        data = {'name': 'Banana', 'address': 'China'}
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Banana')

    def test_update_invalid_company(self):
        url = reverse('company-detail', kwargs={'pk': self.company1.id})
        response = self.client.put(url, data={'name': ''})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_valid_company(self):
        url = reverse('company-detail', kwargs={'pk': self.company1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_company(self):
        url = reverse('company-detail', kwargs={'pk': 9999})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
