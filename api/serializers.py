# api/serializers.py
from rest_framework import serializers

from stations.models import MeteorologicalStation


class MetereologicalStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeteorologicalStation
        fields = ('altitude', 'latitude', 'longitude', 'city',
                  'state', 'created_date', 'edited_date')
