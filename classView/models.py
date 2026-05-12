from django.db import models
from funcView.models import Students

class Citizen(Students):
    National_Id = models.IntegerField()

class FileUpload(models.Model):
    file = models.FileField(upload_to='media/')
