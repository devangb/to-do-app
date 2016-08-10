from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoItem(models.Model):
    description = models.CharField(max_length=50)
    done = models.BooleanField(default=False)
    owner = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_at = models.DateTimeField()

    def __str__(self):
        return self.description
