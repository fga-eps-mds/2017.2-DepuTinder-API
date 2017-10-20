from django.test import TestCase
from .views import parlamentarians
from rest_framework.test import APIRequestFactory

class ParlamentariansViewTest(TestCase):
    def testRequestResponse(self):
        STATUS_CODE_APPROVED = int(200)
        factory = APIRequestFactory()
        request = factory.get('/parlamentarians')
        response = parlamentarians(request)
        self.assertEqual(response.status_code, STATUS_CODE_APPROVED)
