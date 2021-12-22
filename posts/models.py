from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime

from users.models import SWOUser


class Project(models.Model):
    """
    Project model is used to organize projects.
    """

    name = models.CharField(max_length=512, null=False, blank=False)
    description = models.CharField(max_length=256, null=False, blank=False, default="A short description")
    moderators = models.ManyToManyField(SWOUser, related_name="moderator")
    developers = models.ManyToManyField(SWOUser, related_name="dev")
    visibility = models.BooleanField(null=False, default=True)
    public = models.BooleanField(null=False, default=False)
    source_code_url = models.URLField(null=True, blank=True, default=None)
    deployment_code = models.URLField(null=True, blank=True, default=None)
    created = models.DateTimeField(null=False, auto_now_add=True)

    def __str__(self):
        return self.name


class Page(models.Model):
    """
    Page model handles individual content pages.
    """

    name = models.CharField(max_length=512, null=False, blank=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created = models.DateTimeField(null=False, auto_now_add=True)
    updated = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return self.project.name + " - " + self.name


class Post(models.Model):
    """
    Posts model is used to structure posts made by users under various
    projects.
    """

    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=True, blank=True)
    order = models.IntegerField(default=1)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(null=False, auto_now_add=True)
    updated = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return "-".join([self.page.project.name, self.page.name, str(self.order)])

    def check_content(self):
        if self.body is None and self.image.instance.pk is None:
            raise ValidationError("Body or image must be present")

    def save(self, *args, **kwargs):
        self.check_content()
        super(Post, self).save(*args, **kwargs)