from .views import questionnaire
from django.test import TestCase
from rest_framework.test import APIRequestFactory

class  QuestionnaireTest(TestCase):
  def RequestFromAPI(self):
    STATUS_CODE_APPROVED = int(201)

    factory = APIRequestFactory()
    request = factory.get('http://myjson.com/nc619')
    response = questionnaire(request)

    self.assertEqual(response.status_code, STATUS_CODE_APPROVED)

  def RequestFromApp(self):
    STATUS_CODE_APPROVED = int(201)

    factory = APIRequestFactory()
    request = factory.get('/questionnaire/')
    response = PropositionsView(request)

    self.assertEqual(response.status_code, STATUS_CODE_APPROVED)
