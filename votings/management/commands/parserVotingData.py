from votings.models import Votings
from django.core.management import BaseCommand
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.parseData()

    def parseData(self):
        for i in range(10):
            votings, create = Votings.objects.get_or_create(
                candidateVote = random.randrange(1,4),
                candidateID = fake.random_number(),
                propositionID = random.randrange(0,10),
            )
            if (created):
                self.stdout.write("Voting " + votings.candidateID + " salvo com sucesso!")
                self.stdout.write("Voting " + votings.propositionID + " salvo com sucesso!")
                self.stdout.write("Voting " + votings.candidateVote + " salvo com sucesso!")
            else:
                self.stdout.write("Voting " + votings.candidateID + " erro ao salvar!")
                self.stdout.write("Voting " + votings.propositionID + " erro ao salvar!")
                self.stdout.write("Voting " + votings.candidateVote + " erro ao salvar!")
