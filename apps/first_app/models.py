from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Travel(models.Model):
    destination = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    travelDateFr = models.CharField(max_length=8)
    travelDateTo = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
