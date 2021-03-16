from django.contrib import admin
from .models import *


for i in (Announcement,Agent,Contact,Client, Navbar,About):
    admin.site.register(i)

