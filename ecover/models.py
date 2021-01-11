from django.db import models

class Announcement(models.Model):
    region = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    addres = models.CharField(max_length=30)
    price = models.FloatField()
    property_type = models.CharField(max_length=20)
    views = models.TextField(max_length=60)

    def __str__(self):
        return self.property_type

# Create your models here.
