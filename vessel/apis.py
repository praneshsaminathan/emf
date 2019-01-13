import logging

from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import VesselInfo
from .serializers import VesselInfoSerializer


LOGGER = logging.getLogger('api')


class VesselInfoViewSet(ModelViewSet):
    queryset = VesselInfo.objects.all()
    serializer_class = VesselInfoSerializer
    permission_classes = (AllowAny,)
    throttle_scope = 'vessel-info'

    def list(self, request):
        try:
            client_address = request.META['HTTP_X_FORWARDED_FOR']
        except:
            client_address = request.META['REMOTE_ADDR']
        print(client_address)
        return super().list(self, request)

