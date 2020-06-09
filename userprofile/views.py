from django.shortcuts import render,redirect

from django.views.generic import TemplateView

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from .forms import CreateUserForm
from .models import Profile


def register(request):
    
    form = CreateUserForm()

    if request.method == "POST":
        
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            return redirect('login')
    return render(request, 'accregister.html', {'form':form})

def loginpage(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            return redirect('login')
            messages.error(request, 'username or password is incorrect')


    return render(request, 'acclogin.html')   

def logoutuser(request):
    logout(request)
    return redirect('login')