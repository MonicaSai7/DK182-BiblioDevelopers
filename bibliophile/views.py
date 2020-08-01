from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
# Create your views here.
def home(request):
    return render (request,'home.html')

def login(request):
    
    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        first_name= request.POST['firstname']
        last_name= request.POST['lastname']
        email= request.POST['email']
        username= request.POST['username']
        psw= request.POST['psw']
        pswrepeat= request.POST['pswrepeat']
        user = User.objects.create_user(first_name=first_name,last_name=last_name, password=psw,email=email, username=username)
        user.save()
        print('created')
        return redirect('/')
    else:
     return render(request,'reg.html')

def about(request):
    return render(request,'about.html')
