from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration

# Create your views here.

def showformdata(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print("valid")
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form': fm})

