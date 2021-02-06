from django.shortcuts import render
from django.contrib.auth.models import User
from ecover.models import Announcement, Region, District, Type, Status, View
import json
from django.core import serializers
from PIL import Image
from django.core.files.storage import FileSystemStorage

def personal(request, username):
    announcements = Announcement.objects.filter(person_name=username)
    user = User.objects.filter(username=username)
    return render(request, "personal_area/personal_area.html", {'announcements': announcements, 'user': user})

    
def add(request, username):
    regions = Region.objects.all()
    json_serializer = serializers.get_serializer("json")()
    districts = json_serializer.serialize(District.objects.all(), ensure_ascii=False)
    types = Type.objects.all()
    statuses = Status.objects.all()
    views = View.objects.all()

    if request.method == 'POST':
        title = request.POST['title']
        region_id = request.POST['region_id']
        district_id = request.POST['district_id']
        address = request.POST['address']
        type_id = request.POST['type_id']
        status_id = request.POST['status_id']
        view_id = request.POST['view_id']
        content = request.POST['content']
        image = request.FILES.get('image')
        price = request.POST['price']
        person_name = request.POST['person_name']
        phone = request.POST['phone']

        announcements = Announcement(
            title=title,
            region_id=region_id,
            district_id=district_id,
            address=address,
            type_id=type_id,
            status_id=status_id,
            view_id=view_id,
            content=content,
            image=image,
            price=price,
            person_name=person_name,
            phone=phone
        )
        announcements.save()
      
    return render(request, 'add.html',
        {
            'regions': regions,
            'districts': districts,
            'types': types,
            'statuses': statuses,
            'views': views
        })
