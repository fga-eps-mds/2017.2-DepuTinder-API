import csv
from parlamentarians.models import Parlamentarians
from django.core.management import BaseCommand



class Command(BaseCommand):
    def handle(self, *args, **options):
        parlamentariansFile = open("parlamentariansData.csv", "r")
        csv_reader = csv.reader(parlamentariansFile)
        for row in csv_reader:
            _, created = Parlamentarians.objects.get_or_create(
            parlamentaryPhotoPath = row[0],
            parlamentaryName = row[1],
            parlamentaryUF = row[2],
            parlamentaryPoliticalParty = row[3],
        )
