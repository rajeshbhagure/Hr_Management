from django import forms
from applicant.models import Applicant
from applicant.models import  Application

class DateInput(forms.DateInput):
    input_type = 'date'

class Applicant_Form(forms.ModelForm):
    class Meta:
        model=Applicant
        fields="__all__"
        widgets = {"dob": DateInput}

class ApplicationForm(forms.ModelForm):
    ch=(
        ("Male","Male"),
        ("Female","Female"),
    )

    class Meta:
        model=Application
        fields="__all__"
        widgets = {"dob": DateInput}
    gender=forms.ChoiceField(choices=ch)

