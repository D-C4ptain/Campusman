from django.db import models
from baseapp.data import programs, courses


class StudentDetails(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    admn_no = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    faculty = models.CharField(choices=programs, max_length=200)

    class Meta:
        verbose_name_plural = "Student Details"


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class SchoolPrograms(models.Model):
    course = models.CharField(choices=courses, max_length=200)

    def __str__(self) -> str:
       return self.course

    class Meta:
        verbose_name_plural = "Faculty Courses"


    