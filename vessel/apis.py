from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import VesselInfo
from .serializers import VesselInfoSerializer


class VesselInfoViewSet(ModelViewSet):
    queryset = VesselInfo.objects.all()
    serializer_class = VesselInfoSerializer
    permission_classes = (AllowAny,)
    throttle_scope = 'vessel-info'

