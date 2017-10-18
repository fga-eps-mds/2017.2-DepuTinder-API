import csv
import json
from django.core.management import BaseCommand
from urllib.request import urlopen


class Command(BaseCommand):
    def handle(self, *args, **options):
        url_path = "https://dadosabertos.camara.leg.br/api/v2/deputados?siglaPartido=psol&ordenarPor=nome"
        parlamentariansData = self.request_data(url_path)
        csv_file = self.create_csv_file()
        self.parsing_data_to_csv(csv_file, parlamentariansData)

    def request_data(self, url_path):
        self.stdout.write("Fazendo request dos dados no portal da camara")
        response_data = urlopen(url_path).read().decode('utf-8')
        parlamentariansData = json.loads(response_data)
        return parlamentariansData

    def create_csv_file(self):
        self.stdout.write("Criando arquivo csv")
        parlamentariansFile = open("parlamentariansData.csv", "w")
        csv_file = csv.writer(parlamentariansFile)
        csv_file.writerow(["Link da Foto", "Nome", "UF", "Partido"])
        return csv_file

    def parsing_data_to_csv(self, csv_file, parlamentariansData):
        self.stdout.write("Adicionando dados no arquivo csv")
        for parlamentary in parlamentariansData["dados"]:
            csv_file.writerow([
                parlamentary["urlFoto"],
                parlamentary["nome"],
                parlamentary["siglaUf"],
                parlamentary["siglaPartido"]
            ])
        self.stdout.write("Arquivo csv criado com sucesso!")
