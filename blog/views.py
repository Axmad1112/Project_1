from django.db.models import Q
import django.forms.widgets
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User, Group
from accounts.models import UserDetail
from .models import Post, Post_categories, PostView, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import DetailView, TemplateView, ListView
from taggit.models import Tag
from .forms import PostForm, CommentForm
from django.contrib.auth import get_user
from django.template.defaultfilters import slugify
from ecover.models import Agent, BaseFooter




def blog_single(request, slug):
    posts = get_object_or_404(Post, slug=slug)
    blog_post = Post.objects.all().order_by('-date','-time','-post_view')[:5]
    user = User.objects.all()
    post = Tag.objects.all()
    categories = Post_categories.objects.all()
    footer = BaseFooter.objects.all()
    comments = Comment.objects.filter(post=posts,reply=None)

    post_object=Post.objects.get(slug=slug)
    post_object.post_view = post_object.post_view + 1
    post_object.save()

    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            
           
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            
            if reply_id:
                comment_qs= Comment.objects.get(id=reply_id)

            # new_comment = Comment.objects.create(
            #     post = posts, author = request.user, reply = comment_qs,content=content)
            new_comment = comment_form.save(commit=False)
            new_comment.reply = comment_qs
            new_comment.post = posts     
            new_comment.author = request.user
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
        'footer':footer
    }
    # if request.is_ajax():
    #     html = render_to_string('coments.html',context,request=request)
    #     return JsonResponse({'form':html})
    return render(request, "blog-single.html",context)

def blog(request):
    posts = Post.objects.all().order_by('-date','time')
    footer = BaseFooter.objects.all()
    

    post_list = Post.objects.all().order_by('-date')
    page = request.GET.get('page',1)
    paginator = Paginator(post_list,4)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator,num_pages)
    return render(request, "blog.html", {'posts': posts,'footer':footer})


class BlogCategoriesDetailView(DetailView):
    model = Post
    template_name = 'blog.html'
    def get(self,request,pk):
        posts = Post.objects.filter(categories = pk)
        footer = BaseFooter.objects.all()

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
                'footer':footer
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





