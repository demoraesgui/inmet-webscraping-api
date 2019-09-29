from rest_framework import generics
from rest_pandas import PandasView


from stations.models import MeteorologicalStation
from .serializers import MetereologicalStationSerializer


class MetereologicalStationAPIView(generics.ListAPIView):
    queryset = MeteorologicalStation.objects.all()
    serializer_class = MetereologicalStationSerializer


class MetereologicalStationPandasView(PandasView):
    queryset = MeteorologicalStation.objects.all()
    serializer_class = MetereologicalStationSerializer
    def get_pandas_filename(self, request, format):
        if format in ('csv'):
            # Use custom filename and Content-Disposition header
            return "stations.csv"  # Extension will be appended automatically
        else:
            # Default filename from URL (no Content-Disposition header)
            return None