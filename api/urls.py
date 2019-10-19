# api/urls.py
from django.urls import path

from .views import MetereologicalStationAPIView, MetereologicalStationPandasView, MeteorologicalDataDetailAPIView, MetereologicalStationListAPIView

urlpatterns = [
    path('', MetereologicalStationListAPIView.as_view()),
    path('csv/', MetereologicalStationPandasView.as_view()),
    path('<int:pk>/', MetereologicalStationAPIView.as_view()),
]
