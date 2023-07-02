from django import forms
from django.core import validators

class StudentRegistration(forms.Form):
    # name = forms.CharField(min_length=5, max_length=10, empty_value='Prajwal')
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(widget=forms.PasswordInput, label='Password(again)')

    def clean(self):
        cleaned_data = super().clean()
        valpwd = self.cleaned_data['password']
        valrpwd = self.cleaned_data['rpassword']

        if valpwd != valrpwd:
            raise forms.ValidationError('Password does not match')

