from django.urls import path

from .views import MeteorologicalStationListView

urlpatterns = [
    path('', MeteorologicalStationListView.as_view(), name='home'),
]
