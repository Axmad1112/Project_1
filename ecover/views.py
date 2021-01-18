from django.shortcuts import render
from ecover.models import Announcement, Blog, Agent

def index(request):
    announcements = Announcement.objects.all()
    agents = Agent.objects.all()
    return render(request, "index.html", {'announcements': announcements,'agents': agents})

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

def properties_single(request):
    return render(request, "properties-single.html")

def properties(request):
    announcements = Announcement.objects.all()
    return render(request, "properties.html", {'announcements': announcements})

def services(request):
    return render(request, "services.html")
