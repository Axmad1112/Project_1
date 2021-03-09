from django import forms
from django.forms.widgets import TextInput, PasswordInput, CheckboxInput, EmailInput
from django.contrib.auth.models import User
from ecover.models import Announcement
from .models import UserDetail



class loginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'name': 'username',
            'class': 'form-input',
            'placeholder': 'User Name',
            'required': 'required'
        })
    )
    password = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(attrs={
            'name': 'password1',
            'class': 'form-input',
            'placeholder': 'Password',
            'required': 'required'
        })
    )
   
class registerForm(forms.Form):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'name': 'first_name',
            'class': 'form-input',
            'placeholder': 'First Name',
            'required': 'required'
        })
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'name': 'last_name',
            'class': 'form-input',
            'placeholder': 'Last Name',
            'required': 'required'
        })
    )
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'name': 'username',
            'class': 'form-input',
            'placeholder': 'User Name',
            'required': 'required'
        })
    )
    email = forms.EmailField(
        max_length=30,
        widget=forms.EmailInput(attrs={
            'name': 'email',
            'class': 'form-input',
            'placeholder': 'Email',
            'required': 'required'
        })
    )
    password1 = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(attrs={
            'name': 'password1',
            'class': 'form-input',
            'placeholder': 'Password',
            'required': 'required'
        })
    )
    password2 = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(attrs={
            'name': 'password2',
            'class': 'form-input',
            'placeholder': 'Password',
            'required': 'required'
        })
    )

class EditProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control h6'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }


class ProfileEdit(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['author_image', 'phone']
        widgets = {
            'author_image':forms.FileInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
        }