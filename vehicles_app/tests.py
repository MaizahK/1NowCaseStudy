from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Vehicle
from rest_framework import status

User = get_user_model()

class VehicleTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.other_user = User.objects.create_user(username='otheruser', password='pass')
        self.client.force_authenticate(user=self.user)

    def test_create_vehicle(self):
        data = {'make': 'Toyota', 'model': 'Corolla', 'year': 2020, 'plate': 'XYZ123'}
        response = self.client.post('/api/vehicles/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Vehicle.objects.filter(owner=self.user).exists())

    def test_list_vehicles(self):
        Vehicle.objects.create(owner=self.user, make='Honda', model='Civic', year=2018, plate='ABC')
        response = self.client.get('/api/vehicles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_vehicle(self):
        vehicle = Vehicle.objects.create(owner=self.user, make='Ford', model='Fiesta', year=2015, plate='DEF')
        data = {'make': 'Ford', 'model': 'Focus', 'year': 2016, 'plate': 'DEF'}
        response = self.client.put(f'/api/vehicles/{vehicle.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        vehicle.refresh_from_db()
        self.assertEqual(vehicle.model, 'Focus')

    def test_delete_vehicle(self):
        vehicle = Vehicle.objects.create(owner=self.user, make='Nissan', model='Altima', year=2017, plate='GHI')
        response = self.client.delete(f'/api/vehicles/{vehicle.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Vehicle.objects.filter(id=vehicle.id).exists())

    def test_cannot_access_others_vehicle(self):
        vehicle = Vehicle.objects.create(owner=self.other_user, make='Tesla', model='Model S', year=2022, plate='TESLA')
        response = self.client.get(f'/api/vehicles/{vehicle.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
