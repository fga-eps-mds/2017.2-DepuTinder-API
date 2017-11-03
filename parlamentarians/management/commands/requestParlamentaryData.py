import csv
import json
from django.core.management import BaseCommand
from urllib.request import urlopen


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Fazendo request dos dados no portal da câmara")
        for i in range(1, 7):
            page = str(i)
            url_path = "https://dadosabertos.camara.leg.br/api/v2/deputados?pagina="+page+"&itens=5"
            parlamentariansData = self.request_data(url_path)
            csv_file = self.populate_csv_file(page)
            self.parsing_data_to_csv(csv_file, parlamentariansData)

        self.stdout.write("Dados Obtidos com Sucesso!")

    def request_data(self, url_path):
        response_data = urlopen(url_path).read().decode('utf-8')
        parlamentariansData = json.loads(response_data)
        return parlamentariansData

    def populate_csv_file(self, page):
        first_page = '1'
        csv_file = None
        if page == first_page:
            csv_file = self.create_csv_file()
        else:
            csv_file = self.append_csv_file()

        return csv_file

    def create_csv_file(self):
        parlamentariansFile = open("parlamentariansData.csv", "w")
        csv_file = csv.writer(parlamentariansFile)
        csv_file.writerow(["Link da Foto", "Nome", "UF", "Partido"])
        return csv_file

    def append_csv_file(self):
        parlamentariansFile = open("parlamentariansData.csv", "a")
        csv_file = csv.writer(parlamentariansFile)
        return csv_file

    def parsing_data_to_csv(self, csv_file, parlamentariansData):
        for parlamentary in parlamentariansData["dados"]:
            csv_file.writerow([
                parlamentary["urlFoto"],
                parlamentary["nome"],
                parlamentary["siglaUf"],
                parlamentary["siglaPartido"]
            ])
