from django import forms
from m_app.models import InterModel
from .models import RecruitPost
from applicant.models import Applicant
class DateInput(forms.DateInput):
    input_type = 'date'
class RecruitForm(forms.ModelForm):
    class Meta:
        model=RecruitPost
        fields="__all__"
        widgets = {"start_register": DateInput,"last_register": DateInput}

# class DateInput(forms.DateInput):
#     input_type = 'date'
class AppForm(forms.ModelForm):
    class Meta:
        model=InterModel
        fields="__all__"
        widgets = {"schedule": DateInput}