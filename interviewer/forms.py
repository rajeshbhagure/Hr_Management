from django import forms
from interviewer.models import InterView

class DateInput(forms.DateInput):
    input_type = 'date'

class InterForm(forms.ModelForm):
    choice=(
        ("selected","Selected"),
        ("deselected","Deselected"),
    )
    class Meta:
        model=InterView
        fields="__all__"
        widgets={"schedule_timestamp":DateInput}
    result=forms.ChoiceField(choices=choice)

