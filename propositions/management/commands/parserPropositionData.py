from propositions.models import Propositions
from django.core.management import BaseCommand
from csv import reader as r


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.parseData()

    def parseData(self):
        propositionsFile = open("propositions.csv", "r")
        reader = r(propositionsFile)

        # Go to line 2
        line = next(reader)
        line = next(reader)

        for i in range(10):
            propositions, created = Propositions.objects.get_or_create(
                propositionTitle = line[0],
                propositionDescription = line[2],
                propositionSubTitle = line[1],
                propositionAuthor = line[3],
                propositionLink = line[4],
            )
            if (i < 9):
                line = next(reader)

            if (created):
                self.stdout.write("Proposição " + propositions.propositionTitle + " salvo(a) com sucesso!")
            else:
                self.stdout.write("Proposição " + propositionTitle.propositionTitle + " não foi salvo no banco de dados!")
