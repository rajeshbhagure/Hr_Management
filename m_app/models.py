from django.db import models
from applicant.models import Applicant
# Create your models here.
class RecruitPost(models.Model):
    oppcode=models.IntegerField(primary_key=True,unique=True)
    qualification=models.CharField(max_length=30)
    start_register=models.DateField()
    age=models.IntegerField()
    last_register=models.DateField()
    dept_id=models.CharField(max_length=10)
    position=models.IntegerField()
    description=models.CharField(max_length=100)
    response=models.CharField(max_length=250)
    cno=models.CharField(max_length=13)

class InterModel(models.Model):
    app_id=models.OneToOneField(Applicant,on_delete=models.CASCADE)
    empid=models.IntegerField(unique=True,primary_key=True)
    schedule=models.DateField()


