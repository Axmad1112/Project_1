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

class Views(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Announcement(models.Model):
    title = models.CharField(max_length=10)
    region = models.ForeignKey(Region, on_delete = models.CASCADE, default='Termiz')
    district = models.ForeignKey(District, on_delete = models.CASCADE)
    addres = models.CharField(max_length=30)
    price = models.FloatField()
    type = models.ForeignKey(Type, on_delete = models.CASCADE, blank=True)
    views = models.ForeignKey(Views, on_delete = models.CASCADE, blank=True) 
    text = models.TextField(max_length=60)
    image = models.ImageField(upload_to='picture')
    image_person = models.ImageField(upload_to='image_person')
    person_name = models.CharField(max_length=20)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Agent(models.Model):
    name = models.CharField(max_length=20)
    properties = models.IntegerField()
    image = models.ImageField(upload_to='agent_rasm')
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateField(auto_now=False,)
    number = models.IntegerField()
    text = models.TextField(max_length=50)
    image = models.ImageField(upload_to='blog_rasm')

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
