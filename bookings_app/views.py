from rest_framework import generics, permissions, filters
from .models import Booking
from .serializers import BookingSerializer
from .services import stripe_deposit

# generics APIView inherited to limit endpoints to GET and POST
class BookingViewSet(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['start_date', 'end_date']

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Booking.objects.none()
        qs = Booking.objects.filter(user=self.request.user).order_by('-id')

        from_date = self.request.query_params.get('from')
        if from_date:
            qs = qs.filter(start_date__gte=from_date)
        return qs

    def perform_create(self, serializer):
        stripe_response = stripe_deposit(self.request.user, self.request.data.get("deposit_amount"))
        
        if stripe_response["status"] != "success":
            raise Exception("Payment failed")
        
        serializer.save(user=self.request.user)
