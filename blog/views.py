from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from .models import Blog, Blog_categories, Type
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import DetailView




def blog_single(request, id):
    blogs = get_object_or_404(Blog, pk=id)
    blog_post = Blog.objects.all().order_by('-date','-time')[:5]
    categories = Blog_categories.objects.all()
    types      = Type.objects.all()
    print(blog)
    users_in_group = Group.objects.get(name="Admin").user_set.all()
    is_member = request.user in users_in_group
    context = {
        'blogs': blogs,
        'is_member':is_member,
        'blog_post':blog_post,
        'categories':categories,
        'types':types
    }
    return render(request, "blog-single.html",context)

def blog(request):
    blogs = Blog.objects.all
    users_in_group = Group.objects.get(name="Admin").user_set.all()
    is_member = request.user in users_in_group

    blog_list = Blog.objects.all().order_by('-date')
    page = request.GET.get('page',1)
    paginator = Paginator(blog_list,4)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator,num_pages)
    return render(request, "blog.html", {'blogs': blogs,'is_member':is_member})


class BlogCategoriesDetailView(DetailView):
    model = Blog
    template_name = 'blog.html'
    def get(self,request,pk):
        blogs = Blog.objects.filter(categories = pk)
        users_in_group = Group.objects.get(name="Admin").user_set.all()
        is_member = request.user in users_in_group

        blog_list = Blog.objects.filter(categories=pk).order_by('-date')
        page = request.GET.get('page',1)
        paginator = Paginator(blog_list,4)
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator,num_pages)

        return render(
            self.request,
            self.template_name,
            {
                'blogs':blogs,
                'is_member':is_member
            }
        )
class BlogTypesDetailview(DetailView):
    model = Blog
    template_name = 'blog.html'
    def get(self,request,pk):
        blogs = Blog.objects.filter(types = pk)
        users_in_group = Group.objects.get(name="Admin").user_set.all()
        is_member = request.user in users_in_group

        blog_list = Blog.objects.filter(types=pk).order_by('-date')
        page = request.GET.get('page',1)
        paginator = Paginator(blog_list,4)
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator,num_pages)

        return render(
            self.request,
            self.template_name,
            {
                'blogs':blogs,
                'is_member':is_member
            }
        )