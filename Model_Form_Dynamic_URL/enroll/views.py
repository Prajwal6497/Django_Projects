from django.shortcuts import render
# Create your views here.

# def show_details(request, my_id):
#     return render(request, 'enroll/show.html', {'id': my_id})

def home(request, check):
    print(check)
    return render(request, 'enroll/home.html')

def show_details(request, my_id):
    if my_id == 1:
        student = {'id': my_id, 'name': 'Prajwal'}
    if my_id == 2:
        student = {'id': my_id, 'name': 'Pajji'}
    return render(request, 'enroll/show.html', student)