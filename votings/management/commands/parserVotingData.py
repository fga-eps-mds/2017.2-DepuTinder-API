#!/usr/bin/python3

from votings.models import Votings
from django.core.management import BaseCommand
from parlamentarians.models import Parlamentarians
from propositions.models import Propositions
from csv import reader as r


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.parseData()

    def parseData(self):
        parlamentarians = Parlamentarians.objects.all()
        propositions = Propositions.objects.all()

        votingsFile = open("votings.csv", "r")
        reader = r(votingsFile)

        # skip line 1
        line = next(reader)
        line = next(reader)


        print ("------------" + str(line))
        ID = 1
        for parlamentary in parlamentarians:
            i = 1
            for proposition in propositions:
                # votes.append(line[i])
                if(i <= 10):
                    votings, created = Votings.objects.get_or_create(
                        candidateVote = line[i],
                        candidateID = parlamentary,
                        propositionID = proposition,
                    )
                    i += 1

            line = next(reader)
            ID += 1

            if (created):
                self.stdout.write("Voto " + str(votings) + " salvo com sucesso!")
            else:
                self.stdout.write("NOPE!")
