from django.test import TestCase, Client
from django.shortcuts import reverse

from users.models import SWOUser
from posts.models import Project


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

    def test_docs_view(self):
        """
        Tests if the projects objects are returned correctly.
        """

        # creating three types of project
        project_public = Project.objects.create(name="public project1", public=True, visibilty=True,
                                                description="public project visible to anyone")
        project_private = Project.objects.create(name="private project1", public=False, visibilty=True,
                                                 description="private project but visible to mnnit members")
        project_private_hidden = Project.objects.create(name="private project1", public=False, visibilty=False,
                                                        description="private project visible to only "
                                                                    "moderators and developers")

        project_public.save()
        project_private.save()
        project_private_hidden.save()

        # creating three types of users.

        user = SWOUser.objects.create_user(email="test_user@mnnit.ac.in", password="test@123")
        user_moderator = SWOUser.objects.create_user(email="test_mod@mnnit.ac.in", password="test@123")
        user.is_active = True
        user_moderator.is_active = True
        user.save()
        user_moderator.save()

        # not signed in user should see only public projects

        response = self.client.get(self.root_url + reverse('docs'))

        self.assertEqual(len(response.context["projects"]), 1)

        for project in response.context["projects"]:
            self.assertTrue(project.public)
            self.assertTrue(project.visibilty)

        # signed in user but not a developer or maintainer should see all the public and all the visible projects

        self.client.login(email=user.email, password="test@123")
        response = self.client.get(self.root_url + reverse('docs'))

        self.assertEqual(len(response.context["projects"]), 2)

        for project in response.context["projects"]:
            self.assertTrue(project.visibilty)

        # signed in moderator should see all the projects that are public, visible and user is moderator of
        # checking for developers should also be similar.

        project_private_hidden.moderators.add(user_moderator)
        project_private_hidden.save()

        self.client.logout()
        self.client.login(email=user_moderator.email, password="test@123")

        response = self.client.get(self.root_url + reverse('docs'))

        self.assertEqual(len(response.context["projects"]), 3)
        for project in response.context["projects"]:
            self.assertTrue(project.visibilty or project.moderators.filter(email=user_moderator.email).exists())
