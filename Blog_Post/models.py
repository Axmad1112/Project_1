from django.db import models
from datetime import datetime, date, time
from ecover.models import Agent
from taggit.managers import TaggableManager



class Post_categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        


class Post(models.Model):
    
    title           = models.CharField(max_length=250)
    post_image      = models.ImageField(upload_to='blog_rasm')
    categories      = models.ForeignKey(Post_categories, on_delete=models.CASCADE)
    post_single_image1  = models.ImageField(upload_to='blog_rasm')
    content_header  = models.TextField(max_length=1000)
    post_single_image2  = models.ImageField(upload_to='blog_rasm')
    content_body    = models.TextField(max_length=1000)
    paragraph   = models.TextField(max_length=500)
    agent       = models.ForeignKey(Agent, on_delete=models.CASCADE)
    date        = models.DateField(auto_now_add=True, null=True)
    time        = models.TimeField(auto_now_add=True, null=True)
    slug        = models.SlugField(unique=True, blank=True)
    tags        = TaggableManager()
    

    def __str__(self):
        return self.title


# Create your models here.
