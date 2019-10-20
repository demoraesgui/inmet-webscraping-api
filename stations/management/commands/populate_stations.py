from django.core.management.base import BaseCommand
from stations.webscraper import Webscraper
from stations.models import MeteorologicalStation, MeteorologicalData
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):

        webscraper = Webscraper()
        webscraper.get_stations_info()
        yesterday = (datetime.today() - timedelta(days=1)).strftime("%d/%m/%Y")
        one_year_ago = (datetime.today() - timedelta(days=2)
                        ).strftime("%d/%m/%Y")

        print(yesterday, one_year_ago)

        for index in webscraper.stations:

            station = MeteorologicalStation()
            station.altitude = float(
                webscraper.stations[index]['altitude'].split(' ')[0].replace(',', ''))
            station.latitude = float(webscraper.stations[index]['latitude'])
            station.longitude = float(
                webscraper.stations[index]['longitude'].replace(',', '.'))
            station.state = webscraper.stations[index]['label'].split(' - ')[0]
            station.city = webscraper.stations[index]['label'].split(' - ')[1]

            station.save()
            print(one_year_ago ,yesterday)

            try:
                station_data = webscraper.get_station_data(
                    webscraper.stations[index]['url'], one_year_ago, yesterday)

                for data_sample in station_data:

                    try:
                        meteorological_data_sample = MeteorologicalData()
                        meteorological_data_sample.MeteorologicalStation = station

                        meteorological_data_sample.T_max = float(
                            data_sample['temp_max'])

                        meteorological_data_sample.T_min = float(
                            data_sample['temp_min'])
                        meteorological_data_sample.RH_max = float(
                            data_sample['umid_max'])
                        meteorological_data_sample.RH_min = float(
                            data_sample['umid_min'])
                        meteorological_data_sample.Rn = float(
                            data_sample['radiacao'])
                        meteorological_data_sample.U = float(
                            data_sample['vento_vel'])
                        meteorological_data_sample.P = float(
                            data_sample['pressao'])
                        meteorological_data_sample.Ri = float(
                            data_sample['precipitacao'])
                        meteorological_data_sample.date = datetime.strptime(
                            data_sample['data']+' '+data_sample['hora'], "%d/%m/%Y %H")
                        meteorological_data_sample.save()

                    except:
                        print('Data not valid')

            except:
                print('No data on Station')
