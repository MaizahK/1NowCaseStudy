from django.core.validators import RegexValidator
from rest_framework import serializers
from .models import Vehicle

plate_validator = RegexValidator(r'^[A-Z0-9\-]+$', 'Invalid plate format.')

class VehicleSerializer(serializers.ModelSerializer):
    plate = serializers.CharField(validators=[plate_validator])
    
    class Meta:
        model = Vehicle
        fields = '__all__'
        read_only_fields = ('owner',)

    def validate_year(self, value):
        if value < 1900 or value > 2100:
            raise serializers.ValidationError("Enter a valid year.")
        return value
