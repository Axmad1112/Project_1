from django.contrib import admin
from .models import *


for i in (Announcement,Agent,Blog,Contact, Client, Navbar,About,Region):
    admin.site.register(i)
# Register your models here.

