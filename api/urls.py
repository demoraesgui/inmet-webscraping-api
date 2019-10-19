# api/urls.py
from django.urls import path

from .views import MetereologicalStationAPIView, MetereologicalStationPandasListView, MeteorologicalDataDetailAPIView, MetereologicalStationListAPIView

urlpatterns = [
    path('', MetereologicalStationListAPIView.as_view()),
    path('csv/', MetereologicalStationPandasListView.as_view()),
    path('<int:pk>/', MetereologicalStationAPIView.as_view()),
    path('<int:pk>/data/', MetereologicalStationAPIView.as_view()),
]
