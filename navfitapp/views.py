from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.cache import cache

# Create your views here.
def home(request):
    return render(request, 'home.html')

def loginpage(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm = AuthenticationForm(request, data=request.POST)
            if fm.is_valid():
                uname = request.POST.get('username')
                upass = request.POST.get('password')
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard/')
            else:
                messages.error(request, 'Invalid Username or Password!')
                return render(request, 'login.html', {'form': fm})
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def registerpage(request):
    if request.method == 'POST':
        fm = RegisterForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Registered Successfully!!!')
            fm.save()
            return HttpResponseRedirect('/login/')
    else:
        fm=RegisterForm()
    return render(request, 'register.html', {'form':fm})

def dashboard(request):
    if request.user.is_authenticated:
        user= request.user
        ct = cache.get('count', version=user.pk)
        return render(request, 'dashboard.html', {'user':request.user, 'ct': ct})
    else:
        return HttpResponseRedirect('/login/')

def aboutus(request):
    return render(request, 'about.html')

def plans(request):
    return render(request, 'plans.html')

def contactus(request):
    return render(request, 'contactus.html')
