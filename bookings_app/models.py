from django.db import models
from django.conf import settings
from vehicles_app.models import Vehicle

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    deposit_amount = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
