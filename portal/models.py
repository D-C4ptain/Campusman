from django.db import models
from baseapp.data import Faculty_choices, Actual_programs


class StudentDetails(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    admn_no = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    faculty = models.CharField(choices=Faculty_choices, max_length=200)

    class Meta:
        verbose_name_plural = "Student Details"


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class SchoolPrograms(models.Model):
    name = models.CharField(choices=Actual_programs, max_length=200)

    def __str__(self) -> str:
       return self.name

    class Meta:
        verbose_name_plural = "School Programs"


    