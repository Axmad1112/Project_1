from django.contrib import admin
from .models import Announcement, Agent, Blog


for i in (Announcement,Agent,Blog):
    admin.site.register(i)
# Register your models here.

