from django.urls import path
from . import views



    

urlpatterns = [
    path('blog-single/<int:id>/',views.blog_single, name='blog-single'),
    path('blog/',views.blog, name='blog'),
    path('Categories/<int:pk>', views.BlogCategoriesDetailView.as_view(), name="categories-detail"),
    path('Types/<int:pk>', views.BlogTypesDetailview.as_view(), name="type-detail"),
]
