from questionnaire.models import Questionnaire
from django.core.management import BaseCommand
from faker import Faker
from random import randint

fake = Faker()

QUANTITY_OF_DATA = 10
MIN_ID = 0
MAX_ID = 100

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.parseData()

    def parseData(self):
        # Data to be parsed
        for i in range(QUANTITY_OF_DATA):
            questionnaire, created = Questionnaire.objects.get_or_create(
                questionnaireID = randint(MIN_ID, MAX_ID)
            )

        if (created):
            self.stdout.write("Questionario " + str(questionnaire.questionnaireID) + " salvo com sucesso!")
        else:
            self.stdout.write("Questionario " + str(questionnaire.questionnaireID) + " não foi salvo no banco de dados!")
