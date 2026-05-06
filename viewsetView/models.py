from django.db import models

class Fruits(models.Model):
    Name = models.CharField(max_length=100)