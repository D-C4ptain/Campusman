from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'baseapp/home.html'

class NoticeView(TemplateView):
    template_name = 'baseapp/latest_news.html'

class ProgramView(TemplateView):
    template_name = 'baseapp/programs.html'
