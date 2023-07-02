from django.db import models

# Create your models here.
class Student(models.Model):
    studid = models.IntegerField()
    studname = models.CharField(max_length=50)
    studemail = models.EmailField(max_length=100)
    studdetail = models.CharField(max_length=50)
    stucomment = models.CharField(max_length=50, default='not available')


