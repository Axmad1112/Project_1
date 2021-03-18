from django.urls import path
from . import views



    

urlpatterns = [
    path('blog-single/<int:id>/',views.blog_single, name='blog-single'),
    path('blog/',views.blog, name='blog'),
    path('Categories/<int:pk>', views.BlogCategoriesDetailView.as_view(), name="categories-detail"),
    path('tag/<slug:slug>/', views.tagged, name="tagged"),
]
