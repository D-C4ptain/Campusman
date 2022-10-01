from django.db import models
from baseapp.data import Faculty_choices


class StudentDetails(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    admn_no = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    faculty = models.CharField(choices=Faculty_choices, max_length=200)

    class Meta:
        verbose_name_plural = "StudentDetails"


    def __str__(self):
        return f"{self.first_name} {self.last_name}"



    