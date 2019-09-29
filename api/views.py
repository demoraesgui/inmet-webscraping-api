from rest_framework import generics

from stations.models import MeteorologicalStation
from .serializers import MetereologicalStationSerializer


class MetereologicalStationAPIView(generics.ListAPIView):
    queryset = MeteorologicalStation.objects.all()
    serializer_class = MetereologicalStationSerializer
