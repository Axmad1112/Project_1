from django.contrib import admin
from django.urls import path, include
from . import views



    

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog-single/<slug:slug>/', views.blog_single, name='blog-single'),
    path('Categories/<int:pk>', views.BlogCategoriesDetailView.as_view(), name="categories-detail"),
    path('tag/<slug:slug>/', views.tagged, name="tagged"),
    path('post-search/', views.SearchResultsView.as_view(), name='post-search'),
    
    # path('blog/<slug:slug>/', views.PostDetailView.as_view(), name='detail'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
]
