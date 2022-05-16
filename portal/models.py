from django.db import models

School_choices = (
    ("1","School of Science"),
    ("2","School of Engineering"),
    ("3","School of Art"),
    ("4","School of Infocoms"),
    ("5","School of Business"),
) 

class Student(models.Model):
    Name = models.CharField(max_length=40)
    Admn = models.CharField(max_length=40)
    Faculty = models.CharField(choices=School_choices, max_length=200)
  



    def __str__(self):
        return self.Name



    