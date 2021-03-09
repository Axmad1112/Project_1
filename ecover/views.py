from django.shortcuts import render, redirect, get_object_or_404
from ecover.models import Announcement, Blog, Agent, Type, Contact, About, Client, Navbar, Region, price_value
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.core import serializers
import json
from django.core.mail import send_mail
from .forms import UpdateAddForm
from django.views.generic import DetailView, ListView



def index(request):
    announcements = Announcement.objects.all().order_by('-date','-time')[:5]
    announcement = Announcement.objects.all()
    agents = Agent.objects.all()
    blogs = Blog.objects.all()
    abouts = About.objects.all()
    clients = Client.objects.all()
    types = Type.objects.all()
    navbars = Navbar.objects.all()[:1]
    regions = Region.objects.all()
    user = User.objects.all()
    type = Announcement.objects.filter(type_id="5").count()
    
   
    return render(request, "index.html", {
        'announcements': announcements,
        'announcement':announcement,
        'agents': agents,
        'blogs':blogs,
        'types': types,
        'abouts':abouts,
        'clients':clients,
        'navbars':navbars,
        'regions':regions,
        'user':user,
        'type':type,
    })

def about(request):
    abouts = About.objects.all()
    clients = Client.objects.all()
    return render(request, "about.html",{'abouts':abouts,'clients':clients})

def agent(request):
    agents = Agent.objects.all()
    return render(request, "agent.html", {'agents': agents})

def blog_single(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, "blog-single.html", {'blog': blog})

def blog(request):
    blogs = Blog.objects.all
    

    blog_list = Announcement.objects.all().order_by('-date')
    page = request.GET.get('page',1)
    paginator = Paginator(blog_list,3)
    try:
        announcements = paginator.page(page)
    except PageNotAnInteger:
        announcements = paginator.page(1)
    except EmptyPage:
        announcements = paginator.page(paginator,num_pages)
    return render(request, "blog.html", {'blogs': blogs})


    
def contact(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        email      = request.POST['email']
        message    = request.POST['message']
        msg = first_name + " " + last_name + "\n" + message
        send_mail(
            "Yangi xabar",
            msg,
            "ahmad.togayev.1996@gmail.com",
            [email], 
            fail_silently = False,
        )
        
        contact_user = Contact(

            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message
        )
        contact_user.save()
    return render(request, "contact.html")


def properties_single(request,id):
    announcement = get_object_or_404(Announcement, pk=id)
    return render(request, "properties-single.html", {'announcement': announcement})


def properties(request):
    regions = Region.objects.all()
    types = Type.objects.all()
    announcements = Announcement.objects.all()



    announcement_list = Announcement.objects.all().order_by('-date')
    page = request.GET.get('page',1)
    paginator = Paginator(announcement_list,3)
    try:
        announcements = paginator.page(page)
    except PageNotAnInteger:
        announcements = paginator.page(1)
    except EmptyPage:
        announcements = paginator.page(paginator,num_pages)
     
    context = {
        'announcements': announcements,
        'types':types,
        'regions':regions,
    }

    return render(request, 'properties.html', context)
    
def services(request):
    return render(request, "services.html")

# def search(request):
#     types = Type.objects.all()

#     if request.method == 'GET':
#         title   = request.GET.get('title')
#         type_id = request.GET.get('type_id')
#         price   = request.GET.get('price')
#         result  = Announcement.objects.filter(Q(title__icontains = title | Q(type__icontains = type_id)))

#     print(types,"+++++++++++++++++++++")
#     return render(request, 'properties.html', {'result': result, 'types': types})


def announcement_delete(request,id):
    announcement = get_object_or_404(Announcement, pk=id, person_name=request.user)
    if request.method == 'POST':
        announcement.delete()
        return render(request,'personal_area/personal_area.html')


def update_add(request,id):
    announcement = get_object_or_404(Announcement, pk=id, person_name=request.user)
    form = UpdateAddForm(instance=announcement)
    if request.method == 'POST':

        form = UpdateAddForm(request.POST, request.FILES, instance=announcement)
        
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'update_add.html', context)


class RegionDetailView(DetailView):
    model = Region
    template_name = 'region_properties.html'
    context_object_name = 'region'
    

class AgentDetailView(DetailView):
    model = Agent
    template_name = 'agent_properties.html'
    context_object_name = 'agent'
    def get(self,request,pk):
        announcements = Announcement.objects.filter(agent = pk)
        return render(
            self.request,
            self.template_name,
            {
                'announcements':announcements,
            }
        )

    
    
# def Region(request):
#     blog_list = Announcement.objects.all().order_by('-date')
#     page = request.GET.get('page',1)
#     paginator = Paginator(blog_list,2)
#     try:
#         announcements = paginator.page(page)
#     except PageNotAnInteger:
#         announcements = paginator.page(1)
#     except EmptyPage:
#         announcements = paginator.page(paginator,num_pages)
        
#     return render(request,'region_properties.html',{'announcements':announcements})

class SearchResultsView(ListView):
    model = Announcement
    template_name = 'properties.html'
    

    def get_queryset(self): # new
        
        type=Type.objects.all()
        region=Region.objects.all()
        query = self.request.GET.get('keyvalue')  
        type=self.request.GET.get('type')
        price=self.request.GET.get('price')
        region=self.request.GET.get('region')

        
        print("query keldimi",query)
        print("type keldimi",type)
        print("narx keldimi ko'rilarchi", price)
        print("region keldimi",region)
        
        
        
        
        if query=='' and type=='' and region=='':
            result_list=Announcement.objects.all()
        elif query!='':
            query_list=Q(title__icontains=query)
            if type!='':
                query_list=Q(type__icontains=query) & Q(type_id=type)
            elif region!='':
                query_list=Q(region__icontains=query) & Q(region_id=region)
            result_list=Announcement.objects.filter(query_list).order_by('-date')
        elif type!='':
            query_list=Q(type_id=type)
            if region!='':
                query_list=Q(type_id=type) & Q(region_id=region) 
            result_list=Announcement.objects.filter(query_list).order_by('-date')
        elif region!='':
            query_list=Q(region_id=region) 
            result_list=Announcement.objects.filter(query_list).order_by('-date')
        elif price!='':
            result_list=Announcement.objects.filter(price__gte=price).order_by('-date')
        else:
            query_list=Q(title__icontains=query) & Q(type_id=type) & Q(region_id=region) 
            result_list=Announcement.objects.filter(query_list).order_by('-date')
        return result_list
       



