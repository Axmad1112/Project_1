from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about, name='about'),
    path('agent/',views.agent, name='agent'),
    path('blog-single/',views.blog_single, name='blog-single'),
    path('contact/',views.contact, name='contact'),
    path('blog/',views.blog, name='blog'),
    path('main/',views.main, name='main'),
    path('properties-single/',views.properties_single, name='properties-single'),
    path('properties/',views.properties, name='properties'),
    path('services/', views.services, name='services'),

]