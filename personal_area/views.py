from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from ecover.models import Announcement, Region, District, Type, Status, View
import json
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core import serializers
from PIL import Image
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.db.models import Q



def personal(request, username):
    if request.user.is_authenticated:
        announcements = Announcement.objects.filter(person_name=request.user)
        user = User.objects.filter(username=username)
        return render(request, "personal_area/personal_area.html", {'announcements': announcements, 'user': user})
       
    else:
        return HttpResponse("Bunday sahifa topilmadi !!!")
    
def add(request, username):
    regions = Region.objects.all()
    json_serializer = serializers.get_serializer("json")()
    districts = json_serializer.serialize(District.objects.all(), ensure_ascii=False)
    statuses = Status.objects.all()
    types = Type.objects.all()
    views = View.objects.all()


    if request.method=='POST':

        title = request.POST['title']
        region_id = request.POST['region_id']
        district_id = request.POST['district_id']
        address = request.POST['address']
        type_id = request.POST['type_id']
        view_id = request.POST['view_id']
        status_id = request.POST['status_id']
        content = request.POST['content']
        price = request.POST['price']
        image = request.FILES.get('image')
        phone = request.POST.get('phone', '')

        announcement = Announcement(
            title=title,
            region_id=region_id,
            district_id=district_id,
            address=address,
            type_id=type_id,
            view_id=view_id,
            status_id=status_id,
            price=price,
            content=content,
            image=image,
            phone=phone,
            person_name=request.user
        )
        announcement.save()
    return render(request, 'add.html',
    {
        'regions': regions,
        'districts': districts,
        'statuses': statuses,
        'types': types,
        'views': views
    })

def search(request):
    title = request.GET.get('title')
    results = Announcement.objects.filter(Q(title__icontains = title))
    pages = pagination(request, results, num=1)


    return render(request, 'properties.html', {'items': page[0], 'page_range': page[1]})

