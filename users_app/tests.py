from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

class UserAuthTests(APITestCase):

    def test_register_user_success(self):
        url = reverse('register')
        data = {'username': 'newuser', 'password': 'newpass123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_register_missing_fields(self):
        url = reverse('register')
        data = {'username': ''}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_success(self):
        _ = User.objects.create_user(username='test', password='testpass')
        url = reverse('token_obtain_pair')
        data = {'username': 'test', 'password': 'testpass'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_login_invalid_credentials(self):
        url = reverse('token_obtain_pair')
        data = {'username': 'wrong', 'password': 'wrong'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
