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
        #Para cada parlamentar são gerados 10 votos, cada voto em uma proposição diferente que tem seu id incrementado
        #com a variavel j
        for i in range(10):#trocar 10 pelo numero de parlamentares existentes
            parlamentary = Parlamentarians.objects.get(id=i)
            for j in range(10):
                votings, created = Votings.objects.get_or_create(
                    #Gera inteiro para votação: -1 = NAO / 0 = ME ABSTENHO / 1 = SIM
                    candidateVote = random.randrange(-1,2),
                    candidateID = parlamentary,
                    propositionID = Propositions.objects.get(id=j)
                )
                if (created):
                    self.stdout.write("Voting " + str(votings.candidateVote) + " salvo com sucesso!")
                else:
                    self.stdout.write("Voting " + str(votings.candidateVote) + " erro ao salvar!")
