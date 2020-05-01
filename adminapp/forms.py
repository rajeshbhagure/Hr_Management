from django import forms
from adminapp.models import EmployeeModel

class EmpoyeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = "__all__"
    design=(
        ("MANAGER","Manager"),
        ("HRHEAD","HRhead"),
        ("INTERVIEWER","Interviewer"),
        ("EMPLOYEE","Employee"),
    )
    Designation=forms.ChoiceField(choices=design)
    id=forms.IntegerField(min_value=101)
