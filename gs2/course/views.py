from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def learn_django(request):
    return HttpResponse('Learn Django')

def learn_var(request):
    a = 'Hello Variable'
    return HttpResponse(f'Hi {a}')

def index(request):
    return HttpResponse('Home Page')