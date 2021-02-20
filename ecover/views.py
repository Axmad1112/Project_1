from django.shortcuts import render
from ecover.models import Announcement, Blog, Agent
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage




def index(request):
    announcements = Announcement.objects.all()
    agents = Agent.objects.all()
    return render(request, "index.html", {'announcements': announcements, 'agents': agents})

def about(request):
    return render(request, "about.html")

def agent(request):
    agents = Agent.objects.all()
    return render(request, "agent.html", {'agents': agents})

def blog_single(request):
    return render(request, "blog-single.html")

def blog(request):
    blogs = Blog.objects.all
    return render(request, "blog.html", {'blogs': blogs})

def contact(request):
    return render(request, "contact.html")

def main(request):
    return render(request, "about.html")

def properties_single(request,pk):
    announcement = Announcement.objects.get(id=pk)
    return render(request, "properties-single.html", {'announcement': announcement} )

def properties(request):
    announcement_list = Announcement.objects.all().order_by('-date')
    page = request.GET.get('page',1)
    paginator = Paginator(announcement_list,3)
    try:
        announcements = paginator.page(page)
    except PageNotAnInteger:
        announcements = paginator.page(1)
    except EmptyPage:
        announcements = paginator.page(paginator,num_pages)
    
    index = announcements.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]
    return render(request, 'properties.html', {'announcements': announcements, 'page_range':page_range })
    
def services(request):
    return render(request, "services.html")



