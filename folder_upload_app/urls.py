# urls.py
from django.urls import path
from .views import submit_exam, success

urlpatterns = [
    path('submit_exam/', submit_exam, name='submit_exam'),
    path('success/', success, name='success'),
]
