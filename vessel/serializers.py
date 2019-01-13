from rest_framework import serializers

from .models import VesselInfo


class VesselInfoSerializer(serializers.ModelSerializer):
    """Serializer for Vessel Info"""

    class Meta:
        """docstring for Meta"""
        model = VesselInfo
        exclude = ('created', 'updated', 'mode')