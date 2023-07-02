from django.urls import path, include
from course import views as cv
from fees import views as fv

urlpatterns = [
    path('dj_learn/',cv.django_learn),
]
