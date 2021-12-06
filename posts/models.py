from django.db import models

from users.models import SWOUser


class Project(models.Model):
    """
    Project model is used to organize projects.
    """

    name = models.CharField(max_length=512, null=False, blank=False)
    moderators = models.ManyToManyField(SWOUser)

    def __str__(self):
        return self.name
