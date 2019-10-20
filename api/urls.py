# api/urls.py
from django.urls import path

from .views import MetereologicalStationDetailAPIView, MetereologicalStationDataAPIView, MetereologicalStationPandasListView, MetereologicalStationListAPIView, MeteorologicalStationDataWithInitialDateAPIView, MeteorologicalStationDataWithFinalDateAPIView

urlpatterns = [
    path('', MetereologicalStationListAPIView.as_view()),
    path('csv/', MetereologicalStationPandasListView.as_view()),
    path('<int:pk>/', MetereologicalStationDetailAPIView.as_view()),
    path('<int:pk>/data/', MetereologicalStationDataAPIView.as_view()),
    path('<int:pk>/data/<slug:initial_year>/<slug:initial_month>/<slug:initial_day>',
         MeteorologicalStationDataWithInitialDateAPIView.as_view()),
    path('<int:pk>/data/<slug:initial_year>/<slug:initial_month>/<slug:initial_day>/<slug:final_year>/<slug:final_month>/<slug:final_day>',
         MeteorologicalStationDataWithFinalDateAPIView.as_view())
]
