from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, team, role, access_level, password=None):
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username=username,
            team=team,
            role=role,
            access_level=access_level,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, team, role, access_level, password):
        user = self.create_user(
            username=username,
            team=team,
            role=role,
            access_level=access_level,
            password=password,
        )
        print("correct e")
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    team = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    access_level = models.IntegerField()
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['team', 'role', 'access_level']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
