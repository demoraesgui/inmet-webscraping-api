# api/urls.py
from django.urls import path

from .views import MetereologicalStationAPIView

urlpatterns = [
    path('', MetereologicalStationAPIView.as_view()),
]
