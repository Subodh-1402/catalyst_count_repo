from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homeview(request):
    return render(request, 'index.html')

def loginview(request):
    data = "Welcome To Login Page"
    return render(request, 'app/login.html', context={'data':data})
    # here we parsed data dynamically to the html page.

def registerview(request):
    return render(request,"app/register.html")

