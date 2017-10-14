import csv
import json
from urllib.request import urlopen
from .models import Parlamentarians

#request Data
response_data = urlopen("https://dadosabertos.camara.leg.br/api/v2/deputados?siglaPartido=pt&ordenarPor=nome").read().decode('utf-8')
parlamentariansData = json.loads(response_data)

#creating the file
parlamentariansFile = open("parlamentariansData.csv", "w")
csv_file = csv.writer(parlamentariansFile)
csv_file.writerow(["Link da Foto", "Nome", "siglaUf", "siglaPartido"])

#creating the objects
for deputy in parlamentariansData["dados"]:
    csv_file.writerow([
        deputy["urlFoto"],
        deputy["nome"],
        deputy["siglaUf"],
        deputy["siglaPartido"]
    ])
