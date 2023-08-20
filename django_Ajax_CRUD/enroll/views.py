from django.shortcuts import render
from .forms import StudentUserRegistration
from .models import User
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    fm = StudentUserRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/home.html', {'form': fm, 'stu': stud})

# @csrf_exempt
def save_data(request):
    if request.method == "POST":
        form = StudentUserRegistration(request.POST)
        if form.is_valid():
            name = request.POST["name"]
            email = request.POST["email"]
            password = request.POST["password"]
            usr = User(name = name, email = email, password = password)
            usr.save()
            stud = User.objects.values()
            student_data = list(stud)
            return JsonResponse({'status': 'Save', 'student_data': student_data})
        else:
            return JsonResponse({'status': 0})
        

def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        pi = User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})