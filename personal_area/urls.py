from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('cabinet/', views.personal, name='personal'),
    path('add/', views.add, name='add'),
    

]
