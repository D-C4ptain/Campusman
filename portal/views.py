from re import template
from tkinter import S
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import ICTDetails, FinanceDetails, StudentDetails


class StudentLogin(TemplateView):
    model = StudentDetails
    
class StudentIndexView(DetailView):
    model = StudentDetails
    context_object_name = 'student'
  
