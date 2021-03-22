from django.db.models import Q
import django.forms.widgets
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User, Group
from accounts.models import UserDetail
from .models import Post, Post_categories, PostView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import DetailView, TemplateView, ListView
from taggit.models import Tag
from .forms import PostForm, CommentForm
from django.contrib.auth import get_user
from django.template.defaultfilters import slugify
from ecover.models import Agent




def blog_single(request, slug):
    posts = get_object_or_404(Post, slug=slug)
    blog_post = Post.objects.all().order_by('-date','-time')[:5]
    user = User.objects.all()
    post = Tag.objects.all()
    categories = Post_categories.objects.all()
    comments = posts.comments.all()

    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = posts     
            new_comment.author = request.user
            # Save the comment to the database
            new_comment.save()
            return HttpResponseRedirect(request.path)
    else:
        comment_form = CommentForm()

    context = {
        'posts': posts,
        'blog_post':blog_post,
        'categories':categories,
        'post':post,
        'comments':comments,
        'new_comment':new_comment,
        'comment_form':comment_form,
        'user':user,
    }
    return render(request, "blog-single.html",context)

def blog(request):
    posts = Post.objects.all().order_by('-date','time')
    users_in_group = Group.objects.get(name="Admin").user_set.all()
    is_member = request.user in users_in_group


    post_list = Post.objects.all().order_by('-date')
    page = request.GET.get('page',1)
    paginator = Paginator(post_list,4)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator,num_pages)
    return render(request, "blog.html", {'posts': posts,'is_member':is_member})


class BlogCategoriesDetailView(DetailView):
    model = Post
    template_name = 'blog.html'
    def get(self,request,pk):
        posts = Post.objects.filter(categories = pk)
        users_in_group = Group.objects.get(name="Admin").user_set.all()
        is_member = request.user in users_in_group

        blog_list = Post.objects.filter(categories=pk).order_by('-date')
        page = request.GET.get('page',1)
        paginator = Paginator(blog_list,4)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator,num_pages)

        return render(
            self.request,
            self.template_name,
            {
                'posts':posts,
                'is_member':is_member
            }
        )



def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag)
    context = {
        'posts':posts,
    }
    return render(request, 'blog.html', context)




class SearchResultsView(ListView):
    model = Post
    template_name = 'blog.html'

    def get_queryset(self): # new
        
        query = self.request.GET.get('keyvalue')

        print(query, "++++++++++++++++")
        results = Post.objects.filter(
            Q(title__icontains=query) | Q(content_header__icontains=query) | Q(content_body__icontains=query))
        
        return results

# def home_view(request):
#     posts = Post.objects.order_by('-date')
#     # Show most common tags 
#     common_tags = Post.tags.most_common()[:4]
#     form = PostForm(request.POST)
#     if form.is_valid():
#         newpost = form.save(commit=False)
#         newpost.slug = slugify(newpost.title)
#         newpost.save()
#         # Without this next line the tags won't be saved.
#         form.save_m2m()
#     context = {
#         'posts':posts,
#         'common_tags':common_tags,
#         'form':form,
#     }
#     return render(request, 'new_add.html', context)



