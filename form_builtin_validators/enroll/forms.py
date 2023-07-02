from django import forms
from django.core import validators


def start_with_p(value):
    if value[0] != 'p':
        raise forms.ValidationError('Name should start with p')
    
class StudentRegistration(forms.Form):
    # name = forms.CharField(min_length=5, max_length=10, empty_value='Prajwal')
    name = forms.CharField(validators=[start_with_p])
    email = forms.CharField()

