from django.db import models

from users.models import SWOUser


class Project(models.Model):
    """
    Project model is used to organize projects.
    """

    name = models.CharField(max_length=512, null=False, blank=False)
    description = models.CharField(max_length=256, null=False, blank=False, default="A short description")
    moderators = models.ManyToManyField(SWOUser, related_name="moderator")
    developers = models.ManyToManyField(SWOUser, related_name="dev")
    visibilty = models.BooleanField(null=False, default=True)
    public = models.BooleanField(null=False, default=False)
    source_code_url = models.URLField(null=True, blank=True, default=None)
    deployment_code = models.URLField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Posts model is used to structure posts made by users under various
    projects.
    """

    pass
