from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import user_notes
import pyperclip
from datetime import datetime
import psycopg2

# Create your views here.

prev_text = ''
text = ''
username = ''
res_text = ''
usr = user_notes()

def home(request):
    return render(request,'home.html')

def login(request):  
    global username
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            username = user.username
            auth.login(request, user)
            global usr
            usr.username = user.username
            usr.data = {}
            conn = psycopg2.connect("host=localhost dbname=Bibli user=postgres password=divya003")
            cur = conn.cursor()
            query = str("select session_name,data from user_notes where name = '"+username+"'")
            cur.execute(query)
            all_data = cur.fetchall()
            for i in all_data:
                usr.data[i[0]] = i[1]
            conn.commit()
            return render(request, 'session.html', {'usr':usr})
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/login')
    else:
        return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        first_name= request.POST['firstname']
        last_name= request.POST['lastname']
        email= request.POST['email']
        username= request.POST['username']
        psw= request.POST['psw']
        pswrepeat= request.POST['pswrepeat']
        if psw == pswrepeat:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Usrname taken...')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists...')
                return redirect('/signup')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name, password=psw,email=email, username=username)
                user.save()
                print('created')
                return redirect('/login')
        else:
            print('password not matching...')
            return redirect('/signup')
        return redirect('/login')
    else:
        return render(request,'reg.html')

def about(request):
    return render(request,'about.html')

def get_name():
    return str(datetime.now())[:-7]

def add_note():
    global prev_text
    global text
    global res_text
    text = pyperclip.paste()
    if text != prev_text:
        print(text)
        res_file.write("\n")
        res_file.write(text)
        prev_text = text
        res_text += text
        res_text += "\n"

def session_start(request):
    if request.method == 'POST':
        print('started')
        global file_name
        global res_file
        global res_text
        global prev_text
        global text
        global username
        file_name = str("/Users/kasimahd/Documents/4-2/SIH/result "+get_name()+".txt")
        res_file = open(file_name,"w")
        while True:
            add_note()
            if text == 'end':
                break
        prev_text = ''
        text = ''
        conn = psycopg2.connect("host=localhost dbname=Bibli user=postgres password=divya003")
        cur = conn.cursor()
        cur.execute("insert into user_notes values (%s, %s, %s)",(username, res_text, get_name()))
        res_text = ''
        conn.commit()
        res_file.close()
        return render(request, 'session.html', {'usr':usr})
    return redirect('/session')

def session(request):
    return render (request, 'session.html')

def session_end(request):
    if request.method=='POST':
        print("ending session")
        global text
        global username
        global res_file
        global res_text
        text = 'end'
        res_file.close()
        global usr
        usr.username = username
        usr.data = {}
        conn = psycopg2.connect("host=localhost dbname=Bibli user=postgres password=divya003")
        cur = conn.cursor()
        cur.execute("insert into user_notes values (%s, %s, %s)",(username, res_text, get_name()))
        res_text = ''
        query = str("select session_name,data from user_notes where name = '"+username+"'")
        cur.execute(query)
        all_data = cur.fetchall()
        for i in all_data:
            usr.data[i[0]] = i[1]
        conn.commit()
        return render(request, 'session.html', {'usr':usr})
    return redirect('/session')
    
def data_display(request):
    global usr
    return render(request, 'data_display.html', {'usr':usr})
