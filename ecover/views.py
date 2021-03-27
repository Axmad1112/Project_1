from django.shortcuts import render, redirect, get_object_or_404
from .models import About, Agent, Announcement, BaseFooter, Client, Contact, Navbar, Region, Type
from blog.models import Post
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
    blogs = Post.objects.all().order_by('-date','time')[:4]
    abouts = About.objects.all()
    clients = Client.objects.all()
    types = Type.objects.all()
    navbars = Navbar.objects.all()[:1]
    regions = Region.objects.all()
    user = User.objects.all()
    type = Announcement.objects.filter(type_id="5").count()
    footer = BaseFooter.objects.all()
    
    
   
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
        'footer':footer
    })

def about(request):
    announcement = Announcement.objects.all()
    user = User.objects.all()
    type = Announcement.objects.filter(type_id="5").count()
    abouts = About.objects.all()
    clients = Client.objects.all()
    footer = BaseFooter.objects.all()

    return render(request, "about.html",{
        'abouts':abouts,
        'clients':clients,
        'user':user,
        'type':type,
        'announcement':announcement,
        'footer':footer
    })

def agent(request):
    footer = BaseFooter.objects.all()
    agents = Agent.objects.all()
    return render(request, "agent.html", {'agents': agents,'footer':footer})




    
def contact(request):
    footer = BaseFooter.objects.all()
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
    return render(request, "contact.html",{'footer':footer})


def properties_single(request,id):
    announcement = get_object_or_404(Announcement, pk=id)
    footer = BaseFooter.objects.all()
    return render(request, "properties-single.html", {'announcement': announcement,'footer':footer})


def properties(request):
    regions = Region.objects.all()
    types = Type.objects.all()
    announcements = Announcement.objects.all()

    footer = BaseFooter.objects.all()

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
        'footer':footer
    }

    return render(request, 'properties.html', context)
    
def services(request):
    footer = BaseFooter.objects.all()
    return render(request, "services.html",{'footer':footer})


def announcement_delete(request,id):
    announcement = get_object_or_404(Announcement, pk=id, person_name=request.user)
    if request.method == 'POST':
        announcement.delete()
        return redirect('../../personal')


def update_add(request,id):
    announcement = get_object_or_404(Announcement, pk=id, person_name=request.user)
    form = UpdateAddForm(instance=announcement)
    footer = BaseFooter.objects.all()
    if request.method == 'POST':

        form = UpdateAddForm(request.POST, request.FILES, instance=announcement)
        
        if form.is_valid():
            form.save()
            return redirect('../../personal')
    context = {'form': form,'footer':footer}
    return render(request, 'update_add.html', context)


class RegionDetailView(DetailView):
    model = Region
    template_name = 'region_properties.html'
    def get(self,request,pk):
        announcements = Announcement.objects.filter(region = pk)
        footer = BaseFooter.objects.all()

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
                'footer':footer
            }
        )
    

class AgentDetailView(DetailView):
    model = Agent
    template_name = 'agent_properties.html'
    def get(self,request,pk):
        announcements = Announcement.objects.filter(agent = pk)
        footer = BaseFooter.objects.all()
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
                'footer':footer
                                
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
        


class SearchResultsView(ListView):
    model = Announcement
    template_name = 'properties.html'
    paginate_by = 3
    def get(self,request): # new++
        types=Type.objects.all()
        regions = Region.objects.all()

        query = self.request.GET.get('keyvalue')
        type_query=self.request.GET.get('type_query')
        region = self.request.GET.get('region')
        price_limit = self.request.GET.get('price_limit')

        
        if query:
           results = Announcement.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        
        elif query and type_query:
            results = Announcement.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) & Q(type_id=type_query))
        
        elif query and type_query and region:
            results = Announcement.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) & Q(type_id=type_query) & Q(region_id=region))
        
        elif query and type_query and region and price_limit:
            results = Announcement.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) & Q(type_id=type_query) & Q(region_id=region) & Q(price=price_limit))
        
        elif type_query:
            results = Announcement.objects.filter(Q(type_id=type_query))
        
        elif type_query and region:
            results = Announcement.objects.filter(Q(type_id=type_query) & Q(region_id=region))
        
        elif type_query and region and price_limit:
            results = Announcement.objects.filter(Q(type_id=type_query) & Q(region_id=region) & Q(price=price_limit))
        
        elif region:
            results = Announcement.objects.filter(Q(region_id=region))
        
        elif region and price_limit:
            results = Announcement.objects.filter(Q(region_id=region) & Q(price=price_limit))
        
        elif price_limit:
            results = Announcement.objects.filter(Q(price=price_limit))
        
        else:
            results = Announcement.objects.all()
            

        
        print(query, "bu keyvalue")
        print(type_query, "manabu type id")
        print(region, "bu location")
        print(price_limit," bu narx")

        paginator = Paginator(results, self.paginate_by)
        page = request.GET.get('page',1)
        
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(paginator,num_pages)
        
        print(results)
        context = {
            'types':types,
            'regions':regions,
            'results': results,

        }
        return render(self.request,self.template_name, context)
        




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
        
        
        
        
        
       



