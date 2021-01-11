from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def agent(request):
    return render(request, "agent.html")

def blog_single(request):
    return render(request, "blog-single.html")

def blog(request):
    return render(request, "blog.html")

def contact(request):
    return render(request, "contact.html")

def main(request):
    return render(request, "about.html")

def properties_single(request):
    return render(request, "properties-single.html")

def properties(request):
    return render(request, "properties.html")

def services(request):
    return render(request, "services.html")
