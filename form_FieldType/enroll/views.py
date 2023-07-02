from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration

# Create your views here.

def showformdata(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            agree = fm.cleaned_data['agree']
            roll = fm.cleaned_data['roll']
            print(name, agree, roll)
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form': fm})

