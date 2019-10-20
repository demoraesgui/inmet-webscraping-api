from rest_framework import generics
from rest_framework.views import APIView
from rest_pandas import PandasView
from rest_framework.response import Response
from rest_framework import serializers
from datetime import datetime

from stations.models import MeteorologicalStation, MeteorologicalData
from .serializers import MetereologicalStationDataSerializer, MeteorologicalDataSerializer, MetereologicalStationListSerializer


class MetereologicalStationListAPIView(generics.ListAPIView):
    queryset = MeteorologicalStation.objects.all()
    serializer_class = MetereologicalStationListSerializer


class MetereologicalStationDetailAPIView(generics.RetrieveAPIView):
    queryset = MeteorologicalStation.objects.all()
    serializer_class = MetereologicalStationListSerializer


class MetereologicalStationDataAPIView(generics.RetrieveAPIView):
    queryset = MeteorologicalStation.objects.all()
    serializer_class = MetereologicalStationDataSerializer


class MeteorologicalStationDataWithInitialDateAPIView(APIView):

    def get(self, request, pk, initial_year, initial_month, initial_day):

        initial_date = initial_year + '-' + initial_month + '-' + initial_day

        query = MeteorologicalData.objects.filter(
            MeteorologicalStation__pk=90, date__year=initial_year, date__range=[initial_date, datetime.today().strftime("%Y-%m-%d")])

        serializer = MeteorologicalDataSerializer(query, many=True)

        return Response(serializer.data)


class MeteorologicalStationDataWithFinalDateAPIView(APIView):

    def get(self, request, pk, initial_year, initial_month, initial_day, final_year, final_month, final_day):

        initial_date = initial_year + '-' + initial_month + '-' + initial_day
        final_date = final_year + '-' + final_month + '-' + final_day
        query = MeteorologicalData.objects.filter(
            MeteorologicalStation__pk=90, date__year=initial_year, date__range=[initial_date, final_date])

        serializer = MeteorologicalDataSerializer(query, many=True)

        return Response(serializer.data)


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
