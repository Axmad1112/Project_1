from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from ecover.models import Announcement, Region, District, Type, Status, View
import json
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core import serializers
from PIL import Image
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import AddForm

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


    #     region_id = request.POST['region_id']
    #     district_id = request.POST['district_id']

    #     announcement = Announcement(
    #         region_id=region_id,
    #         district_id=district_id
    #     )
    #     announcement.save()

    #     form=AddForm(request.POST,request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('../')
        
    # else:
    #     form=AddForm()
    # return render(request,'add.html',
    # {
    #     'form':form, 
    #     'regions': regions,
    #     'districts': districts        
    # })


def properties(request,username):
    announcement_list = Announcement.objects.filter(username=username).order_by('-date','-upload_date')
    page = request.GET.get('page',1)
    paginator = Paginator(announcement_list,6)
    try:
        announcements = paginator.page(page)
    except PageNotAnInteger:
        announcements = paginator.page(1)
    except EmptyPage:
        announcements = paginator.page(paginator,num_pages)
    return render(request, 'properties.html', {'username': username, 'announcement': announcement_list })
    
# def upload(request,username):
#     context={}
#     if request.method=='POST':
#         uploaded_file=request.FILES['document']
#         fs=FileSystemStorage() 
#         name=fs.save(uploaded_file.name,uploaded_file)
#         context['url']=fs.url(name)
#     return render(request, 'add.html',context)