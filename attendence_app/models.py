from django.db import models

from django.contrib.auth.models import User
# Create your models here.




class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

