from django.urls import path
from .views import IndexView, NoticeView, ProgramView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('notice/', NoticeView.as_view(), name='notice'),
    path('programs/', ProgramView.as_view(), name='programs'),
]

