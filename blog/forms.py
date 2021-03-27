from django import forms
from .models import Comment, Post
from django.forms.widgets import TextInput, EmailInput, Textarea, FileInput
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content_body',
            'tags'
        ]

class CommentForm(forms.ModelForm):
    
    
    name = forms.CharField(widget = TextInput(attrs={
        'class':'form-control',
        'id':'name'
    
    }))

    email = forms.EmailField(widget = EmailInput(attrs={
        'class':'form-control',
        'id':'email'
    }))


    content = forms.CharField(widget = Textarea(attrs={
        'class':'form-control',
        'id':'message',
        'cols':'40',
        'rows':'2'
    }))


    
    


    class Meta:
        model = Comment
        fields = ['name','email','content']
    

