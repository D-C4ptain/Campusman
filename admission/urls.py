from django.urls import path
from .views import AdmissionView

urlpatterns = [
    path('', AdmissionView.as_view(), name='admission')
]