from django.shortcuts import render, redirect, get_object_or_404
from .models import Announcement, Agent, Type, Contact, About, Client, Navbar, Region
from blog.models import Blog
from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.core import serializers
import json
from django.core.mail import send_mail
from .forms import UpdateAddForm, SearchForm
from django.views.generic import DetailView, ListView, TemplateView






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
    users_in_group = Group.objects.get(name="Admin").user_set.all()
    is_member = request.user in users_in_group
    
   
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
        'is_member':is_member
    })

def about(request):
    announcement = Announcement.objects.all()
    user = User.objects.all()
    type = Announcement.objects.filter(type_id="5").count()
    abouts = About.objects.all()
    clients = Client.objects.all()

    users_in_group = Group.objects.get(name="Admin").user_set.all()
    is_member = request.user in users_in_group
    return render(request, "about.html",{
        'abouts':abouts,
        'clients':clients,
        'user':user,
        'type':type,
        'announcement':announcement,
        'is_member':is_member
    })

def agent(request):
    users_in_group = Group.objects.get(name="Admin").user_set.all()
    is_member = request.user in users_in_group
    agents = Agent.objects.all()
    return render(request, "agent.html", {'agents': agents,'is_member':is_member})




    
def contact(request):
    users_in_group = Group.objects.get(name="Admin").user_set.all()
    is_member = request.user in users_in_group

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
    return render(request, "contact.html",{'is_member':is_member})


def properties_single(request,id):
    announcement = get_object_or_404(Announcement, pk=id)
    users_in_group = Group.objects.get(name="Admin").user_set.all()
    is_member = request.user in users_in_group
    return render(request, "properties-single.html", {'announcement': announcement,'is_member':is_member})


def properties(request):
    regions = Region.objects.all()
    types = Type.objects.all()
    announcements = Announcement.objects.all()

    users_in_group = Group.objects.get(name="Admin").user_set.all()
    is_member = request.user in users_in_group

    announcement_list = Announcement.objects.all().order_by('-date')
    page = request.GET.get('page',1)
    paginator = Paginator(announcement_list,9)
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
        'is_member':is_member
    }

    return render(request, 'properties.html', context)
    
def services(request):
    users_in_group = Group.objects.get(name="Admin").user_set.all()
    is_member = request.user in users_in_group
    return render(request, "services.html",{'is_member':is_member})


def announcement_delete(request,id):
    announcement = get_object_or_404(Announcement, pk=id, person_name=request.user)
    if request.method == 'POST':
        announcement.delete()
        return redirect('../../personal')


def update_add(request,id):
    announcement = get_object_or_404(Announcement, pk=id, person_name=request.user)
    form = UpdateAddForm(instance=announcement)
    users_in_group = Group.objects.get(name="Admin").user_set.all()
    is_member = request.user in users_in_group
    if request.method == 'POST':

        form = UpdateAddForm(request.POST, request.FILES, instance=announcement)
        
        if form.is_valid():
            form.save()
            return redirect('../../personal')
    context = {'form': form,'is_member':is_member}
    return render(request, 'update_add.html', context)


class RegionDetailView(DetailView):
    model = Region
    template_name = 'region_properties.html'
    def get(self,request,pk):
        announcements = Announcement.objects.filter(region = pk)
        users_in_group = Group.objects.get(name="Admin").user_set.all()
        is_member = request.user in users_in_group

        announcement_list = Announcement.objects.filter(region=pk).order_by('-date')
        page = request.GET.get('page',1)
        paginator = Paginator(announcement_list,2)
        try:
            announcements = paginator.page(page)
        except PageNotAnInteger:
            announcements = paginator.page(1)
        except EmptyPage:
            announcements = paginator.page(paginator,num_pages)

        return render(
            self.request,
            self.template_name,
            {
                'announcements':announcements,
                'is_member':is_member
            }
        )
    

class AgentDetailView(DetailView):
    model = Agent
    template_name = 'agent_properties.html'
    def get(self,request,pk):
        announcements = Announcement.objects.filter(agent = pk)
        users_in_group = Group.objects.get(name="Admin").user_set.all()
        is_member = request.user in users_in_group
        agent = Agent.objects.get(pk=pk)
        
        announcement_list = Announcement.objects.filter(agent=pk).order_by('-date')
        page = request.GET.get('page',1)
        paginator = Paginator(announcement_list,6)
        try:
            announcements = paginator.page(page)
        except PageNotAnInteger:
            announcements = paginator.page(1)
        except EmptyPage:
            announcements = paginator.page(paginator,num_pages)
        return render(
            self.request,
            self.template_name,
            {
                'announcements':announcements,
                'is_member':is_member,
                                
            }
        )

    



# def search(request):
#     types=Type.objects.all()
#     regions=Region.objects.all() 

#     keyvalue = request.GET.get('keyvalue')
#     type_id = request.GET.get('type_id')
#     region_id = request.GET.get('region_id')
#     price = request.GET.get('price')

#     print(type_id,"+++++++++")
#     print(region_id, "-----------")

#     results = Announcement.objects.filter(Q(title__icontains=keyvalue) | Q(content__icontains=keyvalue))
#     context = {
#         'types':types,
#         'regions':regions,
#         'price':price,
#         'results': results

#     }
#     return render(request,'search.html', context)
        
class HomePageView(TemplateView):
    template_name = 'index.html'

class SearchResultsView(ListView):
    model = Announcement
    template_name = 'search.html'

    def get_queryset(self): # new
        

        query = self.request.GET.get('keyvalue')
        type_query=self.request.GET.get('type_query')
        

        location = self.request.GET.get('location')

        print(query, "++++++++++++++++")
        print(type_query, "manabu type id")
        print(location, "++++++++++++++++")
        results = Announcement.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(type_id=type_query) | Q(address__icontains=location) | Q(content__icontains=location))
        return results




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

# class SearchResultsView(ListView):
#     model = Announcement
#     template_name = 'properties.html'
    

#     def get_queryset(self): # new
        
#         type=Type.objects.all()
#         region=Region.objects.all()
#         query = self.request.GET.get('keyvalue')  
#         type=self.request.GET.get('type')
#         price=self.request.GET.get('price')
#         region=self.request.GET.get('region')

        
#         print("query keldimi",query)
#         print("type keldimi",type)
#         print("narx keldimi ko'rilarchi", price)
#         print("region keldimi",region)
        
        
        
        
#         if query=='' and type=='' and region=='':
#             result_list=Announcement.objects.all()
#         elif query!='':
#             query_list=Q(title__icontains=query)
#             if type!='':
#                 query_list=Q(type__icontains=query) & Q(type_id=type)
#             elif region!='':
#                 query_list=Q(region__icontains=query) & Q(region_id=region)
#             result_list=Announcement.objects.filter(query_list).order_by('-date')
#         elif type!='':
#             query_list=Q(type_id=type)
#             if region!='':
#                 query_list=Q(type_id=type) & Q(region_id=region) 
#             result_list=Announcement.objects.filter(query_list).order_by('-date')
#         elif region!='':
#             query_list=Q(region_id=region) 
#             result_list=Announcement.objects.filter(query_list).order_by('-date')
#         elif price!='':
#             result_list=Announcement.objects.filter(price__gte=price).order_by('-date')
#         else:
#             query_list=Q(title__icontains=query) & Q(type_id=type) & Q(region_id=region) 
#             result_list=Announcement.objects.filter(query_list).order_by('-date')
#         return result_list
       



