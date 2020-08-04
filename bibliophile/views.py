from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django import forms
import boto3

#s3 = boto3.client('s3')
client = boto3.client('cognito-idp', 'us-east-1')
#bucket_name = "sih-biblio"
#s3n = boto3.resource('s3')
#bucket = s3n.Bucket(bucket_name)

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

def value(request):
    accessToken = request.GET['accessToken']
    print(accessToken)
    cognitoID = client.get_user(AccessToken=accessToken)
    print(cognitoID['Username'])
    return render(request, 'userPage.html')

'''def getAccessToken(request):
    print(request)
    if request.method == 'POST':
        accessToken = request.POST['accessToken']
        print(accessToken)
    render(request, 'userPage.html')'''

