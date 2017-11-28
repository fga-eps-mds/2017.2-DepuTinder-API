from questionnaire.models import Questionnaire
from question.models import Question
from django.core.management import BaseCommand
from faker import Faker
from random import randint

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.parseData()

    def parseData(self):
        # Data to be parsed
        questionnaire, created = Questionnaire.objects.get_or_create(
            maxQuestions = 10,
            totalQuestions = 5,
        )

        if (created):
            self.stdout.write("Questionario " + str(questionnaire.id) + " salvo(a) com sucesso!")
        else:
            self.stdout.write("Questionario " + str(questionnaire.id) + " não foi salvo no banco de dados!")
