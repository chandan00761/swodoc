from django.test import TestCase
from django.contrib.auth import get_user_model

from users.models import SWOUser


class UserTest(TestCase):
    """
    Test class related to users app.
    """
    def test_default_user_model(self):
        """
        Test if the user model used by the application is an instance
        of SWOUser
        :return:
        """
        user_model = get_user_model()
        self.assertIsInstance(user_model, SWOUser)
