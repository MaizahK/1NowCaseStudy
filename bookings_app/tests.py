from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from vehicles_app.models import Vehicle
from .models import Booking
from rest_framework import status
from datetime import date, timedelta

User = get_user_model()

class BookingTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.client.force_authenticate(user=self.user)
        self.vehicle = Vehicle.objects.create(owner=self.user, make='Toyota', model='Corolla', year=2020, plate='BOOK1')

    def test_create_booking(self):
        data = {
            'vehicle': self.vehicle.id,
            'start_date': date.today(),
            'end_date': date.today() + timedelta(days=2)
        }
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Booking.objects.filter(user=self.user).exists())

    def test_create_booking_invalid_dates(self):
        data = {
            'vehicle': self.vehicle.id,
            'start_date': date.today(),
            'end_date': date.today() - timedelta(days=1)
        }
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_bookings(self):
        Booking.objects.create(user=self.user, vehicle=self.vehicle, start_date=date.today(), end_date=date.today())
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_booking_belongs_to_user(self):
        other_user = User.objects.create_user(username='other', password='pass')
        other_vehicle = Vehicle.objects.create(owner=other_user, make='Honda', model='Civic', year=2018, plate='OTH123')
        Booking.objects.create(user=other_user, vehicle=other_vehicle, start_date=date.today(), end_date=date.today())
        response = self.client.get('/api/bookings/')
        self.assertEqual(len(response.data), 0)

    def test_delete_booking(self):
        booking = Booking.objects.create(user=self.user, vehicle=self.vehicle, start_date=date.today(), end_date=date.today())
        response = self.client.delete(f'/api/bookings/{booking.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Booking.objects.filter(id=booking.id).exists())
