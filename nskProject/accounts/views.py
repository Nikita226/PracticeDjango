from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            print("User is not None")
            auth.login(request, user)
            print("Logged in")
            return redirect("index")
        else: 
            print("Invalid credentials")
            return redirect("login")
    else:
        return render(request, "login.html")

def logoutPage(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        confirmpassword = request.POST['confirmpassword']
        if password == confirmpassword:
            if User.objects.filter(username = username).exists():
                print("Username already exists")
                return render(request, "register.html")
            elif User.objects.filter(email = email).exists():
                print("Email already taken")
                return render(request, "register.html")
            else:
                user = User.objects.create_user(username=username,password=password, email=email, first_name=fname, last_name=lname)
                user.save()
                print("User Registered")
                return redirect("login")
        else:
            print("Both password did not match.")
            return render(request, "register.html")
    return render(request, "register.html")