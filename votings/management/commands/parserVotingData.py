from votings.models import Votings
from propositions.models import Propositions
from questionnaire.models import Questionnaire
from parlamentarians.models import Parlamentarians
from django.core.management import BaseCommand
from faker import Faker
from strgen import StringGenerator
import random


fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.parseData()

    def parseData(self):
        for i in range(10):
            votings, created = Votings.objects.get_or_create(
                #Gera inteiro para votação: -1 = NAO / 0 = ME ABSTENHO / 1 = SIM
                candidateVote = random.randrange(-1,2),
                #Gera todos os campos de um objeto Parlamentarians
                candidateID = self.generateParlamentariansInstance(
                    fake.image_url(),
                    StringGenerator('[\l][\l]').render(),
                    fake.name(),
                    StringGenerator('[\l][\l]').render()
                ),
                #Gera todos os campos de um objeto Propositions
                propositionID = self.generatePropositionInstance(
                    random.randrange(1,100),
                    fake.sentence(nb_words=5, variable_nb_words=True, ext_word_list=None),
                    fake.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None),
                    fake.text(max_nb_chars=150, ext_word_list=None),
                    fake.name(),
                    fake.url()
                ),
            )
            if (created):
                self.stdout.write("Voting " + str(votings.candidateVote) + " salvo com sucesso!")
            else:
                self.stdout.write("Voting " + str(votings.candidateVote) + " erro ao salvar!")

    #Instancia Propositions e Questionnaire
    def generatePropositionInstance(self, questionnaireID, propositionTitle, propositionSubTitle, propositionDescription, propositionAuthor, propositionLink):
        questionnaire = Questionnaire()
        proposition = Propositions()
        questionnaire.questionnaireID = questionnaireID
        proposition.questionnaire = questionnaire
        proposition.propositionTitle = propositionTitle
        proposition.propositionSubTitle = propositionSubTitle
        proposition.propositionDescription = propositionDescription
        proposition.propositionAuthor = propositionAuthor
        proposition.propositionLink = propositionLink

    #Instancia Parlamentarians
    def generateParlamentariansInstance(self, parlamentaryPhotoPath, parlamentaryUF, parlamentaryName, parlamentaryPoliticalParty):
        parlamentary = Parlamentarians()
        parlamentary.parlamentaryPhotoPath = parlamentaryPhotoPath
        parlamentary.parlamentaryUF = parlamentaryUF
        parlamentary.parlamentaryName = parlamentaryName
        parlamentary.parlamentaryPoliticalParty = parlamentaryPoliticalParty
