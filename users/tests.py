from .views import getUsers, createUser
from django.test import TestCase
from rest_framework.test import APIRequestFactory

class UsersTest(TestCase):
    def testRequestFromAPI(self):
        STATUS_CODE_APPROVED = int(404)

        factory = APIRequestFactory()
        request = factory.get('/users/')
        response = getUsers(request)

        self.assertEqual(response.status_code, STATUS_CODE_APPROVED)

    def testUserSignUp(self):
        STATUS_CODE_APPROVED = int(200)
        data = {'userName': 'teste', 'userImage': '', 'userEmail': 'teste@teste.com', 'userPassword': 'teste123'}

        factory = APIRequestFactory()
        request = factory.post('/createUser/', data, format='json')
        response = createUser(request)

        self.assertEqual(response.status_code, STATUS_CODE_APPROVED)
