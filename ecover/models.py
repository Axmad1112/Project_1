from django.db import models
from datetime import datetime, date

class Region(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Announcement(models.Model):
    title = models.CharField(max_length=10)
    region = models.ForeignKey(Region,on_delete = models.CASCADE)
    district = models.CharField(max_length=20)
    addres = models.CharField(max_length=30)
    price = models.FloatField()
    type = models.CharField(max_length=10)
    views = models.TextField(max_length=60)
    image = models.ImageField(upload_to='picture')
    image_person = models.ImageField(upload_to='image_person')
    person_name = models.CharField(max_length=20)
    date = models.DateField(auto_now=False)

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
