from django.db import models

# Create your models here.
class Employee(models.Model):
	name = models.CharField(max_length=20)
	age = models.IntegerField()
	sex = models.CharField(max_length=4)
	addr = models.CharField(max_length=100)