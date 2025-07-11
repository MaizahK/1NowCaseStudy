from rest_framework import mixins, viewsets, permissions
from .models import Vehicle
from .serializers import VehicleSerializer

# specific mixins inherited to disallow GET /vehicles/{id} endpoint 
class VehicleViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']    # disallow partial update (PATCH /vehicles/{id})

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Vehicle.objects.none()
        return Vehicle.objects.filter(owner=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
