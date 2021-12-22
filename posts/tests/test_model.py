from django.test import TestCase
from PIL import Image

from posts.models import *
from users.models import SWOUser


class ProjectTests(TestCase):
    """
    Tests related to the Project models are defined here.
    """

    def test_project_model_create(self):
        """
        Tests wheter project model can be created successfully.
        """

        project = Project.objects.create(name="SWODoc", description="A short description of the project.")
        moderator = SWOUser.objects.create_user(email="test@test.com")
        project.moderators.add(moderator)
        project.save()
        self.assertIsInstance(project, Project)
        self.assertEqual(project.name, "SWODoc")
        self.assertTrue(Project.objects.filter(moderators=moderator).exists())


class PageTest(TestCase):
    """
    Tests the functionality of Post object.
    """

    def setUp(self) -> None:
        self.project = Project.objects.create(name="Test project", description="A short description")
        self.project.save()

    def test_object_creation(self):
        """
        Test page object creation.
        """
        page = Page.objects.create(name="Index Page", project=self.project)
        page.save()

        self.assertEqual(page.name, "Index Page")
        self.assertEqual(page.project, self.project)


class PostTest(TestCase):
    """
    Tests the functionality of the Post object.
    """

    def setUp(self) -> None:
        self.project = Project.objects.create(name="Test project", description="A short description")
        self.project.save()
        self.page = Page.objects.create(name="Test page", project=self.project)
        self.page.save()

    def test_object_creation(self):
        """
        Tests object creation.
        """

        # testing body and image both null.
        self.assertRaises(ValidationError, Post.objects.create, page=self.page)

        # testing image null
        post = Post.objects.create(body="This is the post body.", page=self.page)
        post.save()
        self.assertEqual(post.body, "This is the post body.")
