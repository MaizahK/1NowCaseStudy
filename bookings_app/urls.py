from django.urls import path, include
from .views import BookingViewSet

urlpatterns = [
    path('', BookingViewSet.as_view(), name='booking-list-create'),
]
