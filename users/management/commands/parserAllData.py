from django.core.management import BaseCommand
from propositions.management.commands import parserPropositionData
from questionnaire.management.commands import parserQuestionnaireData
from question.management.commands import parserQuestionData
from users.management.commands import parserUserData
from parlamentarians.management.commands import parserParlamentaryData
from votings.management.commands import parserVotingData
import logging

class Command(BaseCommand):

    def handle(self, *args, **options):
        logger = logging.getLogger(__name__)
        # Defining for constants for commands
        parlamentary = parserParlamentaryData.Command
        proposition = parserPropositionData.Command
        questionnaire = parserQuestionnaireData.Command
        question = parserQuestionData.Command
        user = parserUserData.Command
        voting = parserVotingData.Command

        logger.info("Iniciando parser de parlamentares")
        parlamentary.parseData(self)
        logger.info("Parser de parlamentares finalizado!")
        logger.info("Iniciando parser de proposições")
        proposition.parseData(self)
        logger.info("Parser de proposições finalizado!")
        logger.info("Iniciando parser de questionários")
        questionnaire.parseData(self)
        logger.info("Parser de questionários finalizado!")
        logger.info("Iniciando parser de questões")
        question.parseData(self)
        logger.info("Parser de questões finalizado!")
        logger.info("Iniciando parser de usuários")
        user.admin(self)
        user.parserData(self)
        logger.info("Parser de usuários finalizado!")
        logger.info("Iniciando parser de votações")
        voting.parseData(self)
        logger.info("Parser de votações finalizado!")
