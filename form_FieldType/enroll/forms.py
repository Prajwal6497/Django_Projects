from django import forms

class StudentRegistration(forms.Form):
    # name = forms.CharField(min_length=5, max_length=10, empty_value='Prajwal')
    # name = forms.CharField(error_messages={'required':'Enter your name'})
    name = forms.CharField()
    agree = forms.BooleanField(label_suffix=' ', label='I Agree')
    roll = forms.IntegerField(min_value=5)

    #add custom validation for name field
    def clean_name(self):
        val = self.cleaned_data['name']
        if len(val) < 4:
            raise forms.ValidationError('name should be less than 4 letters')
        return val
    