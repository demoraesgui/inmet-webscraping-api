from bs4 import BeautifulSoup
import requests
import re
from base64 import b64decode


class Webscraper():
    stations = {}
    URL_MAP = "http://www.inmet.gov.br/sonabra/maps/pg_mapa.php"

    def get_stations_info(self):

        res = requests.get(self.URL_MAP)
        res.raise_for_status()

        # Separacao das estacoes
        list_markers = (res.text).split("//************* ESTACÃO ")
        del list_markers[0]

        # Inicializacao da lista de dados das estacoes para posterior tratamento
        list_stations = []

        # Scraping dos dados mais brutos de cada estacao
        for i in list_markers:
            st = (i.split("var imagem", maxsplit=1))[0].split("var ")

            # Capturar id da estação
            station_id = str((st[0].split(maxsplit=1))[0])

            # Capturar label da estacao
            station_label = re.search(
                r"(?<=')[^']+(?=')", str(st[-1])).group(0)
            # Capturar html da estacao
            station_html = str(st[2].split("html = ", maxsplit=1)[1])

            # Criacao de dicionario auxiliar de dados de cada estacao
            station_info = {}
            station_info['id'] = station_id
            station_info['label'] = station_label
            station_info['html'] = station_html

            list_stations.append(station_info)

        # Scraping refinado dos dados de cada estacao
        index = 0
        for x in list_stations:

            soup = BeautifulSoup(x['html'], 'html.parser')

            # Captura o link da tabela de dados
            link = ""
            for a in soup.find_all('a'):
                li = a.get('href')
                if (li.find("pg_dspDadosCodigo_sim.php?", 32) != -1):
                    link = li
                    break

            aux = (x['html'].split("<b><b>", maxsplit=1))[
                1].split("<table ", maxsplit=1)

            # Captura lista dos dados geograficos
            localization = ((aux[1].split("</table>", maxsplit=1))
                            [1].split("</font>", maxsplit=1)[0]).split("<br>")

            # Captura demais dados da estacao
            data_aux = ((aux[0].replace("<b>", "")).replace(
                "</b>", "")).split("<br>")
            data = []

            for d in data_aux:
                if (d.find("<a ", 0, 4) == -1) and (d.find("</a>", 0, 4) == -1) and (len(d) > 0):
                    data.append(d)

            # Criacao do objeto estacao para o JSON
            station_data = {}
            details = {}

            details['estacao'] = data[0].split(": ")[1]
            details['codigo_omm'] = data[1].split(": ")[1]

            if (len(data) > 2):
                details['registro'] = data[2].split(": ")[1]
                details['temp_max'] = (data[3].split(": ")[1]).replace("º", "")
                details['temp_min'] = (data[4].split(": ")[1]).replace("º", "")
                details['umidade'] = data[5].split(": ")[1]
                details['pressao'] = data[6].split(": ")[1]
                details['precipitacao'] = data[7].split(": ")[1]
                details['vento_dir'] = (data[8].split(
                    ": ")[1]).replace("º", "graus")
                details['vento_vel'] = data[9].split(": ")[1]
            else:
                details['registro'] = ""
                details['temp_max'] = ""
                details['temp_min'] = ""
                details['umidade'] = ""
                details['pressao'] = ""
                details['precipitacao'] = ""
                details['vento_dir'] = ""
                details['vento_vel'] = ""

            station_data['label'] = x['label']
            station_data['url'] = link
            station_data['latitude'] = (
                localization[1].split(": ")[1]).replace("º", "")
            station_data['longitude'] = (
                localization[2].split(": ")[1]).replace("º", "")
            station_data['altitude'] = localization[3].split(": ")[1]
            station_data['abertura'] = localization[0].split(": ")[1]
            station_data['detalhes'] = details

            self.stations[str(index)] = station_data
            index = index + 1

    def get_station_data(self, url, dtaini, dtafim):

        session = requests.Session()
        request = session.get(url)

        soup = BeautifulSoup(request.text, 'html.parser')

        def has_name_and_value_tag(tag):
            return tag.has_attr('name') and tag.has_attr('value')

        post_data = {}

        for tag in soup.form.find_all(has_name_and_value_tag):
            post_data[tag['name']] = tag['value']

        post_data['dtaini'] = dtaini
        post_data['dtafim'] = dtafim

        post_data['aleaNum'] = b64decode(post_data['aleaValue'])

        request = session.post(url, data=post_data)

        soup = BeautifulSoup(request.text, 'html.parser')

        trs = soup.tbody.find_all('tr')

        headers = ['data', 'hora', 'temp_inst', 'temp_max', 'temp_min', 'umid_inst',
                   'umid_max', 'umid_min', 'pto_orvalho_inst', 'pto_orvalho_max',
                   'pto_orvalho_min', 'pressao', 'pressao_max', 'pressao_min',
                   'vento_direcao', 'vento_vel', 'vento_rajada', 'radiacao',
                   'precipitacao', ]

        rows = [[td.string for td in tr.find_all('td')] for tr in trs]
        stationdata = [dict(zip(headers, row)) for row in rows]

        return stationdata