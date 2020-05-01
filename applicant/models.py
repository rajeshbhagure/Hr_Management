from django.db import models

# Create your models here.
class Applicant(models.Model):
    id=models.IntegerField(unique=True,primary_key=True)
    name=models.CharField(max_length=30)
    dob=models.DateField(max_length=20)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    gender=models.CharField(max_length=10)
    mobile=models.IntegerField(unique=True)
    address=models.CharField(max_length=60)

    def __str__(self):
        return str(self.id)

class Application(models.Model):
    name=models.CharField(max_length=30)
    dob=models.DateField()
    email=models.EmailField(max_length=30,unique=True)
    gender=models.CharField(max_length=30)
    m_no=models.IntegerField()
    address=models.CharField(max_length=30)
    qualification=models.CharField(max_length=30)
    post=models.CharField(max_length=30)
    percentage=models.IntegerField()
    resume=models.FileField(upload_to="document/")





