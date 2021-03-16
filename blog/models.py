from django.db import models
from datetime import datetime, date, time
from ecover.models import Agent



class Blog_categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        

class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Blog(models.Model):
    
    title           = models.CharField(max_length=250)
    blog_image      = models.ImageField(upload_to='blog_rasm')
    categories      = models.ForeignKey(Blog_categories, on_delete=models.CASCADE)
    blog_single_image1  = models.ImageField(upload_to='blog_rasm')
    content_header  = models.TextField(max_length=1000)
    blog_single_image2  = models.ImageField(upload_to='blog_rasm')
    content_body    = models.TextField(max_length=1000)
    paragraph   = models.TextField(max_length=500)
    types       = models.ForeignKey(Type, on_delete=models.CASCADE)
    agent       = models.ForeignKey(Agent, on_delete=models.CASCADE)
    date        = models.DateField(auto_now_add=True, null=True)
    time        = models.TimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title


# Create your models here.
