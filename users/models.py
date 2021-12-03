from django.db import models
from django.contrib.auth.models \
    import AbstractBaseUser, PermissionsMixin, BaseUserManager


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
        kwargs.setdefault("is_superuser", False)
        kwargs.setdefault("is_staff", False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        if not password:
            raise ValueError("Password is required!")
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_staff", True)
        return self._create_user(email=email, password=password, **kwargs)


class SWOUser(AbstractBaseUser, PermissionsMixin):
    """
    SWOUser is used to keep track of the users in the system.
    """

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=512, null=False, blank=False)
    last_name = models.CharField(max_length=512, null=False, blank=False)
    is_staff = models.BooleanField(null=False, default=False)

    objects = SWOUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

