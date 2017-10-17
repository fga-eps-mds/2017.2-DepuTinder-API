from .views import rankingIndex
from django.test import TestCase
from rest_framework.test import APIRequestFactory

class CandidateRankingTest(TestCase):
    def testRequestFromAPI(self):
        STATUS_CODE_APPROVED = int(200)

        factory = APIRequestFactory()
        request = factory.get('/ranking/')
        response = rankingIndex(request)

        self.assertEqual(response.status_code, STATUS_CODE_APPROVED)
