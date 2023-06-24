from django.urls import path

from . import views

urlpatterns = [
    path('candidate/', views.candidate, name='candidate'),
]