from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from ecover.models import Announcement, Region, District, Type, Status, View, Agent
import json
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core import serializers
from PIL import Image
from django.http import HttpResponse




def personal(request, username):
    if request.user.is_authenticated:
        announcements = Announcement.objects.filter(person_name=request.user)
        user = User.objects.filter(username=username)
        
        users_in_group = Group.objects.get(name="Admin").user_set.all()
        is_member = request.user in users_in_group

        announcement_list = Announcement.objects.filter(person_name=request.user).order_by('-date')
        page = request.GET.get('page',1)
        paginator = Paginator(announcement_list,6)
       
        try:
            announcements = paginator.page(page)
        except PageNotAnInteger:
            announcements = paginator.page(1)
        except EmptyPage:
            announcements = paginator.page(paginator,num_pages)
        return render(request, "personal_area/personal_area.html", {'announcements': announcements, 'user': user,'is_member':is_member})
       
    else:
        return HttpResponse("Bunday sahifa topilmadi !!!")
    
def add(request, username):
    users_in_group = Group.objects.get(name="Admin").user_set.all()
    is_member = request.user in users_in_group
            
    regions = Region.objects.all()
    json_serializer = serializers.get_serializer("json")()
    districts = json_serializer.serialize(District.objects.all(), ensure_ascii=False)
    statuses = Status.objects.all()
    types = Type.objects.all()
    views = View.objects.all()
    agents = Agent.objects.all()

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
        agent_id = request.POST['agent_id']

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
            person_name=request.user,
            agent_id = agent_id
        )
        announcement.save()
    return render(request, 'add.html',
            {
                'regions': regions,
                'districts': districts,
                'statuses': statuses,
                'types': types,
                'views': views,
                'agents':agents,
                'is_member':is_member
            })
        






