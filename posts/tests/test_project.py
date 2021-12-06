from django.test import TestCase

from posts.models import Project
from users.models import SWOUser


class ProjectTests(TestCase):
    """
    Tests related to the Project models are defined here.
    """

    def test_project_model_create(self):
        """
        Tests wheter project model can be created successfully.
        """

        project = Project.objects.create(name="SWODoc")
        moderator = SWOUser.objects.create_user(email="test@test.com")
        project.moderators.add(moderator)
        self.assertIsInstance(project, Project)
        self.assertEqual(project.name, "SWODoc")
        self.assertGreater(Project.objects.filter(moderators=moderator).count(), 0)
