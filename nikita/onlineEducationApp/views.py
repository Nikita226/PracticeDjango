from django.contrib import messages
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth, User
from django.contrib.auth import logout

from .models import Data
from .forms import DataForm, SubjectForm

def new(request):
    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            print("Data Form saved")
            return redirect('/')
        else:
            print("Form did not saved") 
    else:
        form = DataForm()
        print("Error occuredddd!!!!!")
        return render(request, "data.html", {"form" : form})


def subject(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/')
        else:
            print("Form did not save")
            return render(request, "subject.html", {"form" : form})
    else:
        form = SubjectForm()
        print("Error occured during submitting subject !!!!")
        return render(request, "subject.html", {"form" : form})

def index(request):
    return render(request, "index.html", {"datas": Data.objects.all()})



def homee(request):
    return render(request, "home.html", {'name':'Nikita'})

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            print("User is not none")
            auth.login(request, user)
            print("Logged in")
            return redirect("index")
        else: 
            print("Invalid credentials")
            messages.error(request, "Invalid credentials")
            return redirect("login")
    else:
        return render(request, "login.html")

def registerPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']        
        
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                print("username already taken")
                return render(request, "register.html")

            elif User.objects.filter(email = email).exists():
                print("email already taken")
                messages.error(request, "Email Already taken")
                return render(request, "register.html")

            else:
                user = User.objects.create_user(username=username,password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("User Registered")
                return redirect("login")
        else:
            return render(request, "register.html")
    else:
        return render(request, "register.html")

def logoutPage(request):
    logout(request)
    return redirect('home')