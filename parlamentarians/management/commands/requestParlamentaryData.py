import csv
import json
from django.core.management import BaseCommand
from urllib.request import urlopen


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Fazendo request dos dados no portal da camara")
        response_data = urlopen("https://dadosabertos.camara.leg.br/api/v2/deputados?siglaPartido=psol&ordenarPor=nome").read().decode('utf-8')
        parlamentariansData = json.loads(response_data)

        #creating the file
        self.stdout.write("Abrindo arquivo csv")
        parlamentariansFile = open("parlamentariansData.csv", "w")
        csv_file = csv.writer(parlamentariansFile)
        csv_file.writerow(["Link da Foto", "Nome", "UF", "Partido"])

        #creating the objects
        self.stdout.write("Adicionando dados no arquivo csv")
        for deputy in parlamentariansData["dados"]:
            csv_file.writerow([
                deputy["urlFoto"],
                deputy["nome"],
                deputy["siglaUf"],
                deputy["siglaPartido"]
            ])
        self.stdout.write("Arquivo csv criado com sucesso!")
