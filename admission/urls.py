from django.urls import path
from .views import AdmissionView, AdmissionGssView, AdmissionPssView

urlpatterns = [
    path('', AdmissionView.as_view(), name='admission'),
    path('gss/', AdmissionGssView.as_view(), name='gss'),
    path('pss/', AdmissionPssView.as_view(), name='pss'),
]