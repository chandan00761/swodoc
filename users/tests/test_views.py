from django.test import SimpleTestCase
from django.test.client import Client
from django.shortcuts import reverse
from django.core.exceptions import PermissionDenied


class UserViewsTest(SimpleTestCase):
    """
    Tests related to users app views.
    """
    def setUp(self) -> None:
        self.client = Client()
        self.url = "http://127.0.0.1:8000"

    def test_check_signup(self):

        # tests get forbidden
        response = self.client.get(self.url + reverse("user_signup"))
        self.assertEqual(response.status_code, 403)

        # tests wrong post data
        data = {
            "email_signup": "testemail"
        }
        response = self.client.post(self.url + reverse("user_signup"), data=data)
        self.assertEqual(response.status_code, 400)

        # tests wrong domain
        data = {
            "email_signup": "tastemail@google.com"
        }
        response = self.client.post(self.url + reverse("user_signup"), data=data)
        self.assertEqual(response.status_code, 400)


