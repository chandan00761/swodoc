from django.test import TestCase
from django.contrib import admin

from users.models import SWOUser


class UserAdminTest(TestCase):
    """
    Tests related to User app for Admin Dashboard
    """

    def setUp(self):
        self.site = admin.AdminSite()

    def test_user_model_registered(self):
        """
        Test if SWOUser is registered in the admin site
        """

        self.assertTrue(admin.site.is_registered(SWOUser))
