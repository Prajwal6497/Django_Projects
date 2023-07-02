from django import forms

class StudentRegistration(forms.Form):
    # name = forms.CharField(min_length=5, max_length=10, empty_value='Prajwal')
    name = forms.CharField()
    email = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']
        if len(valname) < 4:
            raise forms.ValidationError('Name should be more than or equal to 4')
        if len(valemail) < 10:
            raise forms.ValidationError('Email should be more than or equal to 10')
        
    