from users.models import Users
from django.core.management import BaseCommand
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.parseData()

    def parseData(self):
        for i in range(10):
            user, created = Users.objects.get_or_create(
                userName = fake.name(),
                userImage = fake.text(),
                userPassword = fake.password(),
                userEmail = fake.email(),
            )
            if (created):
                self.stdout.write("Usuário " + user.userName + " salvo com sucesso!")
            else:
                self.stdout.write("Usuário " + user.userName + " salvo com sucesso!")
