from django.test import TestCase, Client
from django.shortcuts import reverse

from users.models import SWOUser


class WebViewTests(TestCase):
    """
    This tests are related to the website, UI and templates.
    """

    root_url = "http://127.0.0.1:8000"

    def setUp(self) -> None:
        self.client = Client()

    def test_index_works(self):
        """
        test whether index view words properly
        """

        response = self.client.get(self.root_url)
        self.assertEqual(response.status_code, 200)

    def test_signup_get(self):
        """
        test if signup page is rendered correctly or not.
        """

        response = self.client.get(self.root_url + reverse("signup"))
        self.assertEqual(response.status_code, 200)

    def test_signup_post(self):
        """
        test the functionality when signup form is submitted through post
        """

        # test wrong data

        data = {
            "email_signup": "chandan"
        }

        response = self.client.post(self.root_url + reverse("signup"), data=data)
        self.assertEqual(response.status_code, 200)

        data["email_signup"] = "chandan.2020ca021@mnnit.ac.in"

        # test on correct data

        response = self.client.post(self.root_url + reverse("signup"), data=data)
        user = SWOUser.objects.get(email=data["email_signup"])
        self.assertIsNotNone(user)
        self.assertEqual(user.email, data["email_signup"])
        self.assertEqual(response.status_code, 200)

        # test duplicate data insert
        response = self.client.post(self.root_url + reverse("signup"), data=data)
        self.assertEqual(response.status_code, 200)

    def test_login_post(self):
        """
        test the functionality when login form is submitted through post
        """

        SWOUser.objects.create_user(email="test@mnnit.ac.in", password="test12345").save()

        # test wrong data

        data = {
            "email_login": "test@mnnit.ac.in",
            "password": "test"
        }
        response = self.client.post(self.root_url + reverse('login'), data=data)
        self.assertTrue(response.status_code, 200)
