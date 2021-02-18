from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User

class Region(models.Model):
    name = models.CharField(max_length=20)
    

    def __str__(self):
        return self.name
        
class District(models.Model):
    name = models.CharField(max_length=20)
    region_id=models.ForeignKey(Region,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class View(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Announcement(models.Model):
    title       = models.CharField(max_length=10)
    region      = models.ForeignKey(Region, on_delete = models.CASCADE)
    district    = models.ForeignKey(District, on_delete = models.CASCADE)
    address     = models.CharField(max_length=30)
    type        = models.ForeignKey(Type, on_delete = models.CASCADE, blank=True, null=True)
    status      = models.ForeignKey(Status, on_delete=models.CASCADE)
    view        = models.ForeignKey(View, on_delete = models.CASCADE, blank=True) 
    content     = models.TextField(max_length=60)
    image       = models.ImageField(upload_to='picture', blank=True, null=True)
    price       = models.FloatField()
    person_name = models.CharField(max_length=20)
    phone       = models.CharField(max_length=20)
    date        = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Agent(models.Model):
    name        = models.CharField(max_length=20)
    properties  = models.IntegerField()
    agent_image = models.ImageField(upload_to='agent_rasm')
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    title       = models.CharField(max_length=20)
    date        = models.DateField(auto_now=True)
    number      = models.IntegerField()
    text        = models.TextField(max_length=50)
    blog_image  = models.ImageField(upload_to='blog_rasm')

    def __str__(self):
        return self.title

# class Client(models.Model):
#     text = models.TextField(max_length=30)
#     name = models.CharField(max_length=30)
#     specialist = models.CharField(max_length=20)
#     image = models.ImageField(upload_to='client')

#     def __str__(self):
#         return self.name
# Create your models here.
