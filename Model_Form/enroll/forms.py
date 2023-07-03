from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'password', 'email')
        labels = {'name': 'Enter your name', 'password': 'Enter your password', 'email': 'Enter your email'}
        error_messages = {
            'password':{'required': 'Password is mandatory'},
            'name':{'required': 'Enter name is mandatory'}
        }
        widgets = {
            'password': forms.PasswordInput,
            'name': forms.TextInput(attrs={'class':'myclass',
                                           'placeholder': 'yaha naam likhiya'})
        }


