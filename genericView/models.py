from django.db import models

class Animals(models.Model):
    Name = models.CharField(max_length=100)
