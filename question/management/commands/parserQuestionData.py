from question.models import Question
from propositions.models import Propositions
from questionnaire.models import Questionnaire
from django.core.management import BaseCommand

NUMBER_OF_QUESTIONS = 10

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.parseData()

    def parseData(self):
        propositions = Propositions.objects.all()
        questionnaire = Questionnaire.objects.all()

        questionnaire = questionnaire[0]

        for proposition in propositions:
            question, created = Question.objects.get_or_create(
                proposition = proposition,
                questionnaire = questionnaire,
                questionTitle = proposition.propositionTitle,
                questionSubtitle = proposition.propositionSubTitle,
                questionDescription = proposition.propositionDescription,
                questionAuthor = proposition.propositionAuthor,
            )

            if (created):
                self.stdout.write("Questao " + question.questionTitle + " salva com sucesso!")
            else:
                self.stdout.write("Questao " + question.questionTitle + " nao foi salva no banco de dados!")
