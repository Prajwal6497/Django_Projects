from enroll.models import Student
from django.shortcuts import render

# Create your tests here.
def studentinfo(request):
    stud = Student.objects.get(pk=1)
    return render(request, 'enroll/studetails.html', {'stu': stud})