from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about, name='about'),
    path('agent/',views.agent, name='agent'),
    path('blog-single/<int:id>/',views.blog_single, name='blog-single'),
    path('contact/',views.contact, name='contact'),
    path('blog/',views.blog, name='blog'),
    path('properties-single/<int:id>/',views.properties_single, name='properties-single'),
    path('properties/',views.properties, name='properties'),
    path('services/', views.services, name='services'),
    path('delete/<int:id>/', views.announcement_delete, name='delete'),
    path('update_add/<int:id>/', views.update_add, name='update_add'),
    path('Region/<int:pk>', views.RegionDetailView.as_view(), name="region-detail"),
    path('Agent/<int:pk>', views.AgentDetailView.as_view(), name="agent-detail"),
    path('search/', views.SearchResultsView.as_view(), name="search")
]