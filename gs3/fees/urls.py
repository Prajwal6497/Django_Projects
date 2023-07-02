from django.urls import path
from course import views as cv
from fees import views as fv

urlpatterns = [
    path('fees/',fv.django_teach),
]
