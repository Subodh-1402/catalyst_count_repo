from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homeview(request):
    page = "Home"
    return render(request, 'index.html', context={'page':page})

def loginview(request):
    data = "Welcome To Login Page"
    page = "Login"
    return render(request, 'app/login.html', context={'data':data, 'page': page})
    # here we parsed data dynamically to the html page.

def registerview(request):
    page = "Register"
    return render(request,"app/register.html", context={'page':page})

