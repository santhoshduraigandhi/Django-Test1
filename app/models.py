from django.db import models

# Create your models here.
class Bio(models.Model):
    Regnum = models.IntegerField(default=00)
    Name = models.CharField(max_length=50)
    Department = models.CharField(max_length=30)
    Grade = models.CharField(max_length=20, default="Enter Grade")