from django.db import models
from datetime import datetime, date, time
from ecover.models import Agent
from accounts.models import UserDetail
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation



class Post_categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        


class Post(models.Model, HitCountMixin):
    
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
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')
    
    

    def __str__(self):
        return self.title

class PostView(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
# Create your models here.

class Comment(models.Model):
    author   = models.ForeignKey(User, on_delete=models.CASCADE)
    date     = models.DateTimeField(auto_now_add=True)
    post     = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    name     = models.CharField(max_length=20)
    email    = models.EmailField()
    content  = models.TextField()
    active   = models.BooleanField(default=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.name)

