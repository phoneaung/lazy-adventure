from django.urls import path

from . import views

urlpatterns = [
    path('candidate/', views.candidate, name='candidate'),
    path('add-candidate/', views.add_candidate, name='add_candidate'),
]