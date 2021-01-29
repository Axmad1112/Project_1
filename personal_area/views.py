from django.shortcuts import render
from django.contrib.auth.models import User
from ecover.models import Announcement

def personal(request, username):
    announcements = Announcement.objects.filter(person_name=username)
    user = User.objects.filter(username=username)
    return render(request, "personal_area/personal_area.html", {'announcements': announcements, 'user': user})

    


