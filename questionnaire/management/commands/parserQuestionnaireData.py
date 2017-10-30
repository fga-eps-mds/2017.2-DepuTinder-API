from questionnaire.models import Questionnaire
from propositions.models import Propositions
from django.core.management import BaseCommand
from faker import Faker
from random import randint

MIN_ID_QUESTIONNAIRE = 0
MAX_ID_QUESTIONNAIRE = 1
class Command(BaseCommand):
    def handle(self, *args, **options):
        self.parseData()

    def parseData(self):

        proposition = (Propositions.objects.all()[:10].filter())

        # Data to be parsed
        questionnaire, created = Questionnaire.objects.get_or_create(
            questionnaireID = randint(MIN_ID_QUESTIONNAIRE, MAX_ID_QUESTIONNAIRE)
        )

        if (created):
            self.stdout.write("Questionario " + str(questionnaire.questionnaireID) + " salvo com sucesso!")
        else:
            self.stdout.write("Questionario " + str(questionnaire.questionnaireID) + " não foi salvo no banco de dados!")
