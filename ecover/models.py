from django.db import models
from datetime import datetime, date, time
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






class Agent(models.Model):
    name        = models.CharField(max_length=20)
    agent_image = models.ImageField(upload_to='agent_rasm')
    
    def __str__(self):
        return self.name

class Announcement(models.Model):
    price_value = (
    ('5000','5000'),
    ('10000','10000'),
    ('50000','50000'),
    ('100000','100000'),
    ('200000','200000'),
    ('300000','300000'),
    ('400000','400000'),
    ('500000','500000'),
    ('600000','600000'),
    ('700000','700000'),
    ('800000','800000'),
    ('900000','900000'),
    ('1000000','1000000'),
    ('2000000','2000000'),
    )

    title       = models.CharField(max_length=30)
    region      = models.ForeignKey(Region, on_delete = models.CASCADE)
    district    = models.ForeignKey(District, on_delete = models.CASCADE)
    address     = models.CharField(max_length=30)
    type        = models.ForeignKey(Type, on_delete = models.CASCADE, null=True)
    status      = models.ForeignKey(Status, on_delete=models.CASCADE)
    view        = models.ForeignKey(View, on_delete = models.CASCADE, blank=True) 
    content     = models.TextField(max_length=60)
    image       = models.ImageField(upload_to='picture', blank=True, null=True)
    price       = models.CharField(choices=price_value, max_length=50, blank=False)
    person_name = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    date        = models.DateField(auto_now_add=True, blank=True)
    time        = models.TimeField(auto_now_add=True)
    agent       = models.ForeignKey(Agent, on_delete = models.CASCADE, null=True)
    phone       = models.CharField(max_length=20, default="+998", null=True, blank=True)
    
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
    title       = models.CharField(max_length=50, blank=True)
    text        = models.CharField(max_length=50, blank=True)
    nav_image   = models.ImageField(upload_to='body_rasm')
    
    def __str__(self):
        return self.title

class About(models.Model):
    title       = models.CharField(max_length=30)
    content     = models.CharField(max_length=150)
    about_image1= models.ImageField(upload_to='about')
    about_image2= models.ImageField(upload_to='about')
    branches    = models.IntegerField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name  = models.CharField(max_length=20, blank=True, null=True)
    email      = models.EmailField(blank=True, null=True)
    message    = models.CharField(max_length=150, blank=True, null=True)
    address    = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.first_name



class BaseFooter(models.Model):
    twitter_link = models.CharField(max_length=50, blank=True, null=True)
    facebook_link = models.CharField(max_length=50, blank=True, null=True)
    instagram_link = models.CharField(max_length=50, blank=True, null=True)
    telegram_link = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.phone