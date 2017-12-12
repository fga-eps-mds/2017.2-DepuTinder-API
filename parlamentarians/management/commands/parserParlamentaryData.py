import csv
from parlamentarians.models import Parlamentarians
from django.core.management import BaseCommand



class Command(BaseCommand):
    def handle(self, *args, **options):
        self.parseData()

    def parseData(self):
        parlamentariansFile = open("parlamentariansData.csv", "r")
        csv_reader = csv.reader(parlamentariansFile)
        row = next(csv_reader) # Jumping the header
        for row in csv_reader:
            parlamentary, created = Parlamentarians.objects.get_or_create(
                parlamentaryPhotoPath = row[0],
                parlamentaryName = row[1],
                parlamentaryUF = row[2],
                parlamentaryPoliticalParty = row[3],
            )
            if (created):
                self.stdout.write("Deputado(a) " + parlamentary.parlamentaryName + " salvo(a) com sucesso!")
            else:
                self.stdout.write("Deputado(a) " + parlamentary.parlamentaryName + " não foi salvo no banco de dados!")
