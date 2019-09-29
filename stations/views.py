from django.views.generic import ListView

from .models import MeteorologicalStation


class MeteorologicalStationListView(ListView):
    model = MeteorologicalStation
    template_name = 'meteorologicalstation_list.html'
