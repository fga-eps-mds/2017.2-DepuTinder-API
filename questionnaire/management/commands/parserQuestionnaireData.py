from questionnaire.models import Questionnaire
from propositions.models import Propositions
from django.core.management import BaseCommand
from faker import Faker
from random import randint

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.parseData()

    def parseData(self):
        proposition = Propositions.objects.all()

        # Data to be parsed
        questionnaire, created = Questionnaire.objects.get_or_create(
            questionnaireID = 0
        )

        if (created):
            self.stdout.write("Questionario " + str(questionnaire.questionnaireID) + " salvo com sucesso!")
        else:
            self.stdout.write("Questionario " + str(questionnaire.questionnaireID) + " não foi salvo no banco de dados!")
