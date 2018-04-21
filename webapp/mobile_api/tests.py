from django.test import TestCase

# Create your tests here.
from users.models import UserProfile
from django.test.client import Client
import json

session_user = Client()

class LoginTestCase(TestCase):
    def setUp(self):
        user = UserProfile.objects.create(
            username='me@k2a.in',
            phno='1234567891',
            email='me@k2a.in',
            first_name='Admin User'
        )
        user.set_password('1234')
        user.save()


    def test_login(self):
        """Authenticate user"""
        response = session_user.post('/api/v1/login', json.dumps({
            'username': 'me@k2a.in',
            'password': '1234',
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200, "Login Failed")
        self.assertIsNotNone(response)
