from users.models import Users
from django.core.management import BaseCommand
from faker import Faker
from cryptography.fernet import Fernet

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.parseData()

    def oneUser(self):
        key = b'8YECmO6MCuZ0Lm887BkLlhqF_SvVb58TvbPohNfTwrk='
        cipher_suite = Fernet(key)
        encrypt_password = cipher_suite.encrypt('calebe'.encode('UTF-8'))

        user, created = Users.objects.get_or_create(
            userName = 'Calebe',
            userImage = '',
            userPassword = encrypt_password,
            userEmail = 'c@c.com',
        )

        if (created):
            self.stdout.write("Usuário " + user.userName + " salvo com sucesso!")
        else:
            self.stdout.write("Usuário " + user.userName + " não foi salvo no banco de dados!")


    def parseData(self):
        key = b'8YECmO6MCuZ0Lm887BkLlhqF_SvVb58TvbPohNfTwrk='
        cipher_suite = Fernet(key)
        encrypt_password = cipher_suite.encrypt(fake.password().encode('UTF-8'))

        for i in range(10):
            user, created = Users.objects.get_or_create(
                userName = fake.name(),
                userImage = fake.text(),
                userPassword = encrypt_password,
                userEmail = fake.email(),
            )
            if (created):
                self.stdout.write("Usuário " + user.userName + " salvo com sucesso!")
            else:
                self.stdout.write("Usuário " + user.userName + " não foi salvo no banco de dados!")
