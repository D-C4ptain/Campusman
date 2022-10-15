from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class AdmissionView(TemplateView):
    template_name = 'admission/admission_procedure.html'