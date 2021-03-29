from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from ecover.models import Announcement
from .forms import loginForm, registerForm, EditProfile, ProfileEdit
from django.contrib.auth.decorators import login_required
from .models import UserDetail


def sign_up(request):
    if request.method == 'POST':
        register_form = registerForm(request.POST)
        if register_form.is_valid():
            first_name = register_form.cleaned_data['first_name']
            last_name = register_form.cleaned_data['last_name']
            username = register_form.cleaned_data['username']
            email = register_form.cleaned_data['email']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']


            if password1==password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"Foydalanuvchi nomi mavjud boshqa nom kiritng !!!")
                    return redirect('sign_up')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Elektron pochta mavjud')
                    return redirect('sign_up')
                else:
                    user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    UserDetail.objects.create(user=user).save()
            else:
                messages.info(request,"Parollar bir biriga to'g'ri kelmaydi !!!")
                return redirect('sign_up')
           
            user = auth.authenticate(username=username, password=password1)
            auth.login(request, user)
               
            if request.user.is_staff:
                return redirect('../' + username)
            else:
                return redirect('../')
    else:
        register_form = registerForm()   
    return render(request, 'accounts/sign_up.html', {'form': register_form })

def sign_in(request):
    if request.method=='POST':
        login_form = loginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                if request.user.is_staff:
                    return redirect('../' + username + 'cabinet')
                else:
                    return redirect('../')
            else:
                messages.info(request, 'Foydalanuvchi nomi yoki parol xato !!!')
                return redirect('sign_in')
    else:
        login_form = loginForm()

    return render(request, 'accounts/sign_in.html',{'form': login_form })

def logout(request):
    auth.logout(request)
    return redirect('/')

    
@login_required
def editprofile(request):
    if request.method == 'POST':
        edit_form = EditProfile(request.POST, instance=request.user)
        p_form  = ProfileEdit(request.POST, request.FILES, instance=request.user.userdetail)
        if edit_form.is_valid() and p_form.is_valid():                            
            edit_form.save()
            p_form.save()
            messages.info(request, "Muvaffaqiyatli yakunlandi!")
            return redirect('profile')
    else:
        edit_form = EditProfile(instance=request.user)
        p_form = ProfileEdit(instance=request.user.userdetail)   
    return render(request, 'profile.html', {'form': edit_form,'p_form':p_form })



# def editprofile(request):
#     if request.method == 'POST':
#         edit_form = EditProfile(request.POST, instance=request.user)
#         p_form  = ProfileEdit(request.POST, request.FILES, instance=request.user.announcement)
#         if edit_form.is_valid() and p_form.is_valid():
#             edit_form.save()
#             p_form.save()
#     else: 
#         edit_form = EditProfile(instance=request.user)
#         p_form  = ProfileEdit(instance=request.user.announcement)
#     return render(request, 'edit_profile.html', {'edit_form':edit_form, 'p_form': p_form})