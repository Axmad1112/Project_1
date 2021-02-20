from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import loginForm, registerForm, EditForm

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
            else:
                messages.info(request,"Parollar bir biriga to'g'ri kelmaydi !!!")
                return redirect('sign_up')
           
            user = auth.authenticate(username=username, password=password1)
            auth.login(request, user)
               
            return redirect('../../' + username)
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
                return redirect('../' + username)
            else:
                messages.info(request, 'Foydalanuvchi nomi yoki parol xato !!!')
                return redirect('sign_in')
    else:
        login_form = loginForm()

    return render(request, 'accounts/sign_in.html',{'form': login_form })

def logout(request):
    auth.logout(request)
    return redirect('/')

def edit_view(UpdateView):
    if request.method == 'POST':
        edit_form = EditForm(request.POST)
        if register_form.is_valid():
            first_name = edit_form.cleaned_data['first_name']
            last_name = edit_form.cleaned_data['last_name']
            username = edit_form.cleaned_data['username']
            email = edit_form.cleaned_data['email']
            password1 = edit_form.cleaned_data['password1']
            password2 = edit_form.cleaned_data['password2']

            

            if password1==password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"Foydalanuvchi nomi mavjud boshqa nom kiritng !!!")
                    return redirect('sign_up')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Elektron pochta mavjud')
                    return redirect('edit_profile')
                else:
                    user = User.objects.update_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                    user.save()
            else:
                messages.info(request,"Parollar bir biriga to'g'ri kelmaydi !!!")
                return redirect('edit_profile')
           
            user = auth.authenticate(username=username, password=password1)
            auth.login(request, user)
               
            return redirect('../../' + username)
    else:
        edit_form = EditForm()   
    return render(request, 'personal_area/personal_area', {'form': edit_form })



