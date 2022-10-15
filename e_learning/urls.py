from django.urls import path
from .views import E_learningView

urlpatterns = [
    path('lms/', E_learningView.as_view(), name='lms'),
]

