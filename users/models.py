from django.db import models
from django.contrib.auth.models \
    import AbstractUser, PermissionsMixin, BaseUserManager
from django.utils.translation import ugettext_lazy as _


class SWOUserManager(BaseUserManager):
    """
    SWOUserManger is the default manager of SWOUser which is used
    to create user objects.
    """

    def _create_user(self, email, password, **kwargs):
        """
        Creates a new user with provided email and password.
        """

        if not email:
            raise ValueError("Email is required!")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **kwargs):
        """
        Helper function to create users.
        sets is_staff, is_superuser, is_active to False by default
        """
        kwargs.setdefault("is_superuser", False)
        kwargs.setdefault("is_staff", False)
        kwargs.setdefault("is_active", False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        if not password:
            raise ValueError("Password is required!")
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_active", True)
        return self._create_user(email=email, password=password, **kwargs)


class SWOUser(AbstractUser):
    """
    SWOUser is used to keep track of the users in the system.
    """
    username = None
    email = models.EmailField(_('Email Address'), unique=True)

    objects = SWOUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.email

    def get_name(self):
        return self.first_name + " " + self.last_name
