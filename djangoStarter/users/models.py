from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

class dbEntry(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries')