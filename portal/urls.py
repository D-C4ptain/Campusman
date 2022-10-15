from django.urls import path 
from .views import *

urlpatterns = [
    path('student/<int:pk>/', StudentIndexView.as_view(), name='student-portal')
   
]