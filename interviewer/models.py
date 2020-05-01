from django.db import models
from applicant.models import Applicant



# Create your models here.class
class InterView(models.Model):

    i_id=models.IntegerField(primary_key=True)
    interviewer=models.IntegerField()
    schedule_timestamp=models.DateField()
    result=models.CharField(max_length=20)
    applicant_id=models.OneToOneField(Applicant,on_delete=models.CASCADE)

