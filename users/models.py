from django.db import models

class Seeker(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)