from django.db import models

class dbEntry(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)