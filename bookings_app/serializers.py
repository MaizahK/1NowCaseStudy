from rest_framework import serializers
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
            vehicle=vehicle,
            start_date__lt=end,
            end_date__gt=start
        ).exists()

        if overlap:
            raise serializers.ValidationError("This vehicle is already booked for these dates.")
    
        return data
