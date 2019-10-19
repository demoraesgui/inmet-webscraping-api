from rest_framework import generics
from rest_pandas import PandasView


from stations.models import MeteorologicalStation, MeteorologicalData
from .serializers import MetereologicalStationDataSerializer, MeteorologicalDataSerializer, MetereologicalStationListSerializer


class MetereologicalStationListAPIView(generics.ListAPIView):
    queryset = MeteorologicalStation.objects.all()
    serializer_class = MetereologicalStationListSerializer


class MetereologicalStationAPIView(generics.RetrieveAPIView):
    queryset = MeteorologicalStation.objects.all()
    serializer_class = MetereologicalStationDataSerializer


class MeteorologicalDataDetailAPIView(generics.RetrieveAPIView):
    queryset = MeteorologicalData.objects.all()
    serializer_class = MeteorologicalDataSerializer


class MetereologicalStationPandasListView(PandasView):
    queryset = MeteorologicalStation.objects.all()
    serializer_class = MetereologicalStationListSerializer

    def get_pandas_filename(self, request, format):
        if format in ('csv'):
            # Use custom filename and Content-Disposition header
            return "stations.csv"  # Extension will be appended automatically
        else:
            # Default filename from URL (no Content-Disposition header)
            return None
