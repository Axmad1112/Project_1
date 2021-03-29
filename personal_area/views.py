from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from ecover.models import Agent, Announcement, BaseFooter, District, Region, Status, Type, View
import json
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core import serializers
from PIL import Image
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import Http404


@login_required
def personal(request, username):
    if request.user.is_staff:
        user = User.objects.filter(username=username)
        announcements = Announcement.objects.filter(person_name=request.user)
        
        footer = BaseFooter.objects.all()

        announcement_list = Announcement.objects.filter(person_name=request.user).order_by('-date')
        page = request.GET.get('page',1)
        paginator = Paginator(announcement_list,6)
        
        try:
            announcements = paginator.page(page)
        except PageNotAnInteger:
            announcements = paginator.page(1)
        except EmptyPage:
            announcements = paginator.page(paginator,num_pages)
        return render(request, "personal_area/personal_area.html", {'announcements': announcements,'user': user,'footer':footer})
    else:
        return HttpResponse("<h1>Ta'qiqlangan sahifaga kirishga urindingiz !!!</h1>") 

@login_required
def add(request, username):
    if request.user.is_staff:
        user = User.objects.get(username=username)
        footer = BaseFooter.objects.all()
                
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
                    'footer':footer,
                    'user':user
                })
    else:
        return HttpResponse("<h1>Siz mumkin bo'lmagan sahifaga kirishga urindingiz !!!</h1>")           





