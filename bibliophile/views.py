from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
# Create your views here.
def home(request):
    return render (request,'home.html')

def login(request):
    
    return render(request,'login.html')

def signup(request):
   
     return render(request,'reg.html')

def about(request):
    return render(request,'about.html')

def userPage(request):
    return render(request, 'userPage.html')



