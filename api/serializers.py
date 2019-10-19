# api/serializers.py
from rest_framework import serializers

from stations.models import MeteorologicalStation, MeteorologicalData


class MeteorologicalDataSerializer(serializers.ModelSerializer):
    # MeteorologicalStation = MetereologicalStationSerializer
    class Meta:
        model = MeteorologicalData
        fields = ('MeteorologicalStation', 'T_max', 'T_min', 'RH_max',
                  'RH_min',    'Rn',    'U',    'P',    'Ri',    'date')

class MetereologicalStationListSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeteorologicalStation
        fields = ('id', 'altitude', 'latitude', 'longitude', 'city',
                  'state', 'created_date', 'edited_date')

class MetereologicalStationSerializer(serializers.ModelSerializer):
    stationData = MeteorologicalDataSerializer(many=True, read_only=True)

    class Meta:
        model = MeteorologicalStation
        fields = ('id', 'altitude', 'latitude', 'longitude', 'city',
                  'state', 'created_date', 'edited_date', 'stationData')
