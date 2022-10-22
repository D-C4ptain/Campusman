from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class AdmissionView(TemplateView):
    template_name = 'admission/admission_procedure.html'
    
class AdmissionGssView(TemplateView):
    template_name = 'admission/admission_gss.html'
    
class AdmissionPssView(TemplateView):
    template_name = 'admission/admission_pss.html'