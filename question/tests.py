from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .views import question

class QuestionViewTest(TestCase):

    def testRequestResponse(self):
        STATUS_CODE_APPROVED = int(200)
        factory = APIRequestFactory()
        request = factory.get('/question')
        response = question(request)
        self.assertEqual(response.status_code, STATUS_CODE_APPROVED)
