from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration

# Create your views here.

def thankyou(request):
    return render(request, 'enroll/success.html')

def showformdata(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            print(name,email)
            return HttpResponseRedirect('/regi/success/')
       
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form': fm})

