# api/urls.py
from django.urls import path

from .views import MetereologicalStationAPIView, MetereologicalStationPandasView

urlpatterns = [
    path('', MetereologicalStationAPIView.as_view()),
    path('csv/',MetereologicalStationPandasView.as_view())
]
