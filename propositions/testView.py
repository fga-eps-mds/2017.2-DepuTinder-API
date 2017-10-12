from .views import PropositionsView
from django.test import TestCase
from rest_framework.test import APIRequestFactory

class PropositionsViewTest(TestCase):
  def testRequestFromAPI(self):
    STATUS_CODE_APPROVED = int(201)

    factory = APIRequestFactory()
    request = factory.get('https://api.myjson.com/bins/m7f4x')
    response = PropositionsView(request)

    self.assertEqual(response.status_code, STATUS_CODE_APPROVED)

  def testRequestFromApp(self):
    STATUS_CODE_APPROVED = int(201)

    factory = APIRequestFactory()
    request = factory.get('/propositions')
    response = PropositionsView(request)

    self.assertEqual(response.status_code, STATUS_CODE_APPROVED)
