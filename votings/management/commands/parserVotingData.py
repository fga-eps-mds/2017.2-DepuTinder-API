from votings.models import Votings
from propositions.models import Propositions
from questionnaire.models import Questionnaire
from parlamentarians.models import Parlamentarians
from django.core.management import BaseCommand
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.parseData()

    def parseData(self):
        parlamentarys = Parlamentarians.objects.all()
        propositions = Propositions.objects.all()

        for parlamentary in parlamentarys:
            for proposition in propositions:
                votings, created = Votings.objects.get_or_create(
                    #Gera inteiro para votação: -1 = NAO / 0 = ME ABSTENHO / 1 = SIM
                    candidateVote = random.randrange(-1,2),
                    candidateID = parlamentary,
                    propositionID = proposition,
                )
                if (created):
                    self.stdout.write("Voting " + str(votings.candidateVote) + " salvo com sucesso!")
                else:
                    self.stdout.write("Voting " + str(votings.candidateVote) + " erro ao salvar!")
