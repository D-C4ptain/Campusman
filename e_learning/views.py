from django.shortcuts import render


from django.views.generic import TemplateView

class E_learningView(TemplateView):
    template_name = 'e_learning/lms.html'


