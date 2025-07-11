from rest_framework import serializers
from django.db.models import Q
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ('user',)

    def validate(self, data):
        vehicle = data['vehicle']
        start = data['start_date']
        end = data['end_date']

        if end < start:
            raise serializers.ValidationError("End date must be after start date.")
        
        # prevent double bookings
        overlap = Booking.objects.filter(
            vehicle=vehicle
        ).filter(
            ~(
                Q(end_date__lt=start) | Q(start_date__gt=end)
            )
        ).exists()

        if overlap:
            raise serializers.ValidationError("This vehicle is already booked for these dates.")
    
        return data
