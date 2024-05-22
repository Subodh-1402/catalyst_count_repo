from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sampleview(request):
    return HttpResponse("welcome to Django web application")