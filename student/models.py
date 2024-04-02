from django.db import models
from django.urls import reverse


# Create your models here.
class details (models.Model):
    name =models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    year = models.IntegerField((""))
    email = models.EmailField()
    course= models.CharField(max_length=100)
    
    
class Placement (models.Model):
    name =models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    location= models.CharField(max_length=100)
    photo =models.ImageField(upload_to="photo/%Y/%m/%d/")
    



