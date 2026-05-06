from django.db import models

class Students(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Department = models.CharField(max_length=100)
    Created_At = models.DateTimeField(auto_now_add=True)
