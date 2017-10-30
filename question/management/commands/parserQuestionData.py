from question.models import Question
from propositions.models import Propositions
from django.core.management import BaseCommand

NUMBER_OF_QUESTIONS = 10

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.parseData()

    def parseData(self):
        propositions = Propositions.objects.all()

        for proposition in propositions:
            question, created = Question.objects.get_or_create(
                questionTitle = proposition.propositionTitle,
                questionSubtitle = proposition.propositionSubTitle,
                questionDescription = proposition.propositionDescription,
                questionAuthor = proposition.propositionAuthor,
                questionLink = proposition.propositionLink,
            )

        if (created):
            self.stdout.write("Questao " + question.questionTitle + " salva com sucesso!")
        else:
            self.stdout.write("Questao " + question.questionTitle + " nao foi salva no banco de dados!")
