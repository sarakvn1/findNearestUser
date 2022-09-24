import json

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

from loguru import logger
from django.db.models.signals import post_delete
from django.dispatch import receiver

from main.managers import UserManager


class BaseModel(models.Model):
    created_time = models.DateTimeField('Created Time', auto_now_add=True)
    updated_time = models.DateTimeField('Updated Time', auto_now=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser, PermissionsMixin,BaseModel):
    username = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    location = models.JSONField(blank=True,null=True,default=dict)
    USERNAME_FIELD = 'username'

    objects = UserManager()

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return f"{self.id}-{self.username}"