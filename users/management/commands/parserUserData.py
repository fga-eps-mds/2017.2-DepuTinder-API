from users.models import Users
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from faker import Faker
from django.contrib.auth.models import User

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.parseData()

    def admin(self):
        user = User.objects.create_user(username='admin', email='admin@admin.com', password='admin123', is_superuser=True)
        user.save()

        users, created = Users.objects.get_or_create(
            user = user,
            userImage = fake.text(),
        )

        if created:
            print(user.username)

    def parseData(self):
        for i in range(10):
            user = User.objects.create_user(username=fake.name(), email=fake.password(), password=fake.email())
            user.save()

            users, created = Users.objects.get_or_create(
                user = user,
                userImage = fake.text(),
            )

            if created:
                self.stdout.write("Usuário " + users.user.username + " salvo com sucesso!")
            else:
                self.stdout.write("Usuário " + users.user.username + " não foi salvo no banco de dados!")
