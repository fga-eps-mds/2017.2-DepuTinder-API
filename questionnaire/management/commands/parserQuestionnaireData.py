from questionnaire.models import Questionnaire
from question.models import Question
from django.core.management import BaseCommand
from faker import Faker
from random import randint

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.parseData()

    def parseData(self):
        question = Question.objects.all()
        questionnaire = Questionnaire.objects.all()

        # Data to be parsed
        for question in questionnaire:
            questionnaire, created = Questionnaire.objects.get_or_create(
                questionsFK = question.id
            )

            if (created):
                self.stdout.write("Questionario " + questionnaire.id + " salvo(a) com sucesso!")
            else:
                self.stdout.write("Questionario " + questionnaire.id + " não foi salvo no banco de dados!")
