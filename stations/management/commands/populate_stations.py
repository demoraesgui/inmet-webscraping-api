from django.core.management.base import BaseCommand
from stations.webscraper import Webscraper
from stations.models import Meteorological_Station


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):

        webscraper = Webscraper()
        webscraper.get_stations_info()
        
        for index in webscraper.stations:
            
            station = Meteorological_Station()
            station.altitude = float(
                webscraper.stations[index]['altitude'].split(' ')[0].replace(',', ''))
            station.latitude = float(webscraper.stations[index]['latitude'])
            station.longitude = float(webscraper.stations[index]['longitude'].replace(',','.'))
            station.state = webscraper.stations[index]['label'].split(' - ')[0]
            station.city = webscraper.stations[index]['label'].split(' - ')[1]

            station.save()
            
