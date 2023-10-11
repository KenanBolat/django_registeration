# from django.contrib.auth.models import AbstractUser
#
#
# class User(AbstractUser):
#     pass


import os

from django.conf import settings
from django.db import models
from django.contrib.auth.models import (

    AbstractUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self, email, username, password=None, **extra_fields):
        """Create, save and return a new user"""
        if not email:
            raise ValueError('User must have an email')
        user = self.model(email=self.normalize_email(email), username=username,   **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, username, password):
        """Create and return new superuser"""
        user = self.create_user(email,  username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)


class User(AbstractUser, PermissionsMixin):
    """User in the system"""

    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    blocked = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
