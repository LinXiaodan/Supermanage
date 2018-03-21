# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models


class User(models.Model):
    user_level = models.IntegerField()
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
