from email.policy import default
from django.db import models
from baseapp.data import programs, courses


class StudentDetails(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    admn_no = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    faculty = models.CharField(choices=programs, max_length=200, default="Science")
    course = models.CharField(choices=courses, max_length=200, default="CSC")

    class Meta:
        verbose_name_plural = "Student Details"


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ICTDetails(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "ICT Personnels"


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class FinanceDetails(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "Finance Officers"


    def __str__(self):
        return f"{self.first_name} {self.last_name}"