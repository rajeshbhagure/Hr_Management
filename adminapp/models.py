from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    id=models.IntegerField(unique=True,primary_key=True,)
    Emp_name=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    contactno=models.CharField(unique=True,max_length=12)
    Designation=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=30)