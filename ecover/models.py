from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User

class Region(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='region_image')

    

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


price_value = (
    ('5000','5000'),
    ('10000','10000'),
    ('500000','500000'),
    ('1000000','1000000'),
    ('2000000','2000000'),
    ('3000000','3000000'),
    ('4000000','4000000'),
    ('5000000','5000000'),
    ('6000000','6000000'),
    ('7000000','7000000'),
    ('8000000','8000000'),
    ('9000000','9000000'),
    ('10000000','10000000'),
    ('20000000','20000000'),
)

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
    price       = models.CharField(choices=price_value, max_length=50, blank=False)
    person_name = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    phone       = models.CharField(max_length=20, default="+")
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

class Client(models.Model):
    text = models.TextField(max_length=100)
    name = models.CharField(max_length=30)
    specialist = models.CharField(max_length=20)
    image = models.ImageField(upload_to='client')

    def __str__(self):
        return self.name
# Create your models here.

class Navbar(models.Model):
    title       = models.CharField(max_length=50)
    text        = models.CharField(max_length=50)
    nav_image   = models.ImageField(upload_to='body_rasm')
    
    def __str__(self):
        return self.title

class About(models.Model):
    title       = models.CharField(max_length=30)
    content     = models.CharField(max_length=150)
    about_image1= models.ImageField(upload_to='about')
    about_image2= models.ImageField(upload_to='about')
    population  = models.IntegerField()
    properties  = models.IntegerField()
    average_house = models.IntegerField()
    branches    = models.IntegerField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=20)
    email      = models.EmailField()
    message    = models.CharField(max_length=150)
    
    def __str__(self):
        return self.first_name

