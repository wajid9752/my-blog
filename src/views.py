from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from .forms import *
from custom_lib import login_lib , authentication_library
# Create your views here.
   

def home(request):
    all_blogs= blog.objects.all().order_by('-date')
    return render(request, 'home.html', {'all_blogs': all_blogs})
   
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have been registered')
            return redirect('user-login')
        else:
            messages.success(request, f'{form.errors}')
            return redirect('register')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # user = authenticate(request, username=username, password=password)
        user=login_lib(username,password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('home')
        else:
            return redirect('user-login')
    else:
        return render(request, 'login.html')


def log_out(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')



def add_blog(request):
    check=authentication_library(request)  
    if not check:
        return redirect('user-login')
    
    form = AddBlog()
    if request.method == 'POST':
        form = AddBlog(request.POST)
        if form.is_valid():
            fr=form.save(commit=False)
            fr.user = request.user
            fr.save()
            messages.success(request, 'added successfully')
            return redirect('home')
    return render(request, 'blog.html', {'form': form})

def update_blog(request,pk):
    check=authentication_library(request)  
    if not check:
        return redirect('user-login')
    blog_obj = blog.objects.get(pk=pk)
    form = AddBlog(instance=blog_obj)
    if request.method == 'POST':
        form = AddBlog(request.POST , instance=blog_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'updated successfully')
            return redirect('profile')
    return render(request, 'blog.html', {'form': form})    

def delete_blog(request,pk):
    check=authentication_library(request)  
    if not check:
        return redirect('user-login')
    blog_obj = blog.objects.get(pk=pk)
    messages.success(request, f'Your blog {blog_obj.title} deleted successfully')
    blog_obj.delete()
    messages.success(request, 'deleted successfully')
    return redirect('profile')


def profile(request):
    check=authentication_library(request)  
    if not check:
        return redirect('user-login') 
    
    all_blogs= blog.objects.filter(user=request.user)
    return render(request, 'profile.html', {'all_blogs': all_blogs})    