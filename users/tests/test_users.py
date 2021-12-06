from django.test import TestCase
from django.contrib.auth import get_user_model

from users.models import SWOUser, SWOUserManager


class UserTest(TestCase):
    """
    Test class related to users app.
    """

    def test_default_user_model(self):
        """
        Test if the user model used by the application is an instance
        of SWOUser i.e SWOUser is made the default User model for the
        application.
        """

        user_model = get_user_model()
        self.assertIs(user_model, SWOUser)

    def test_user_manager_set(self):
        """
        Tests if the user model is using the correct manager i.e.
        whether SWOUser is using SWOUserManager
        """

        user_model = get_user_model()
        self.assertIsInstance(user_model._default_manager, SWOUserManager)

    def test_create_user(self):
        """
        Tests if users can be created from SWOUser
        """

        user_model = get_user_model()
        user = user_model.objects.create_user(email="test@test.com")
        self.assertIsInstance(user, SWOUser)
        self.assertEqual(user.email, "test@test.com")

    def test_create_superuser(self):
        """
        Tests if superusers can be created from SWOUser
        """

        user_model = get_user_model()
        user = user_model.objects.create_superuser(email="admin@admin.com", password="pa88w07d@adm!n")
        self.assertIsInstance(user, SWOUser)
        self.assertTrue(user.is_superuser)
        self.assertEqual(user.email, "admin@admin.com")
        self.assertTrue(user.is_staff)
