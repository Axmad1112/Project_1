from django.shortcuts import render, redirect, get_object_or_404
from ecover.models import Announcement, Blog, Agent, Type, Contact, About, Client, Navbar
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.core.mail import send_mail
from .forms import UpdateAddForm
from .filters import AnnouncementFilter

from .forms import SearchForm
from search_views.search import SearchListView
from search_views.filters import BaseFilter



def index(request):
    announcements = Announcement.objects.all()
    agents = Agent.objects.all()
    blogs = Blog.objects.all()
    abouts = About.objects.all()
    clients = Client.objects.all()
    types = Type.objects.all()
    navbars = Navbar.objects.all()
    
    if request.method == 'GET':
        keyvalue = request.GET.get('keyvalue')
        types = request.GET.get('type')
        

   
    return render(request, "index.html", {
        'announcements': announcements,
        'agents': agents,
        'blogs':blogs,
        'types': types,
        'abouts':abouts,
        'clients':clients,
        'navbars':navbars,
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
            "sardorbek.uktamov.1@mail.ru",
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

def main(request):
    return render(request, "about.html")

def properties_single(request,id):
    announcement = get_object_or_404(Announcement, pk=id)
   
    return render(request, "properties-single.html", {'announcement': announcement})


def properties(request):
    announcements = Announcement.objects.all()
    types = Type.objects.all()

    announcement_list = Announcement.objects.all().order_by('-date')
    page = request.GET.get('page',1)
    paginator = Paginator(announcement_list,3)
    try:
        announcements = paginator.page(page)
    except PageNotAnInteger:
        announcements = paginator.page(1)
    except EmptyPage:
        announcements = paginator.page(paginator,num_pages)

    return render(request, 'properties.html', {'announcements': announcements,'types':types})
    
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


class Filter(BaseFilter):
    search_fields = {
        'search_text' : ['title', 'content'],
        'search_price_exact' : { 'operator' : '__exact', 'fields' : ['price'] },
        'search_price_min' : { 'operator' : '__gte', 'fields' : ['price'] },
        'search_price_max' : { 'operator' : '__lte', 'fields' : ['price'] },

    }

class SearchList(SearchListView):
    model = Announcement
    paginate_by = 30
    template_name = "properties.html"
    form_class = SearchForm
    filter_class = Filter