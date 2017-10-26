from propositions.models import Propositions
from django.core.management import BaseCommand
from faker import Faker



class Command(BaseCommand):
    def handle(self, *args, **options):
        self.parseData()

    def parseData(self):
        faker = Faker()
        for i in range(10):
            propositions, created = Propositions.objects.get_or_create(
                propositionTitle = faker.city(),
                propositionSubTitle = faker.state(),
                propositionDescription = faker.text(),
                propositionAuthor = faker.name(),
                propositionLink = faker.url(),
            )
            if (created):
                self.stdout.write("Proposição " + propositions.propositionTitle + " salvo(a) com sucesso!")
            else:
                self.stdout.write("Proposição " + propositionTitle.propositionTitle + " não foi salvo no banco de dados!")
