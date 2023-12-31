from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

def showformdata(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            fdata = User(name=nm, email=em, password=pw)
            fdata.save()
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form': fm})

