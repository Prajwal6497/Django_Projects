from django.db import models

# Create your models here.
class Student(models.Model):
    stuname = models.CharField(max_length=50)
    stuemail = models.EmailField(max_length=40)
    stupass = models.CharField(max_length=30)

    def __str__(self):
        return self.stuname