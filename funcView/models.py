from django.db import models

class Students(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Department = models.CharField(max_length=100)
    Created_At = models.DateTimeField(auto_now_add=True)

class Citizen(Students):
    National_Id = models.IntegerField()

class Animals(models.Model):
    Name = models.CharField(max_length=100)

class Fruits(models.Model):
    Name = models.CharField(max_length=100)