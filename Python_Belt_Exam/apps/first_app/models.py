from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Item(models.Model):
    name = models.CharField(max_length=50)
    added_by = models.ForeignKey(User, related_name = "all_added")  
    date_added = models.DateTimeField(auto_now_add=True)
    all_users = models.ManyToManyField(User, related_name="all_items")