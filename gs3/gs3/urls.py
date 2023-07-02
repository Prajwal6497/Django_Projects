from django.contrib import admin
from django.urls import path, include
from course import views as cv
from fees import views as fv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('co/',include('course.urls')),
    path('fe/',include('fees.urls')),
]
