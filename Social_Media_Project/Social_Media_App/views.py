from random import randint
from django.shortcuts import render,redirect
from Social_Media_App import *
from django.contrib.auth.models import auth,User
from django.contrib import messages
from .models import *
# Create your views here.
def Home(request):
    return render(request, 'home.html')
def Profile(request):
    return render(request, 'profile.html')

def Post(request):
    user_post=User.objects.all()
    print(user_post)
    return render(request, 'post.html',{"post":user_post})
    
def Register(request):
    if request.method == "POST":
        First_Name=request.POST["first_name"]
        Last_Name=request.POST["last_name"]
        Username=request.POST["username"]
        Email=request.POST["email"]
        Password1=request.POST["password1"]
        Password2=request.POST["password2"]
        if Password1==Password2:
            if User.objects.filter(username=Username).exists():
                messages.info(request,'user already exist')
                return redirect('/register')

            elif User.objects.filter(email=Email).exists():
                messages.info(request,'email already exist')
                return redirect('/register')
            
            else:
                user=User.objects.create_user(first_name=First_Name, last_name=Last_Name,username=Username,email=Email,password=Password1)
                user.save()
                # user_otp=randint(100000,999999)
                # UserOTP.objects.create(usr=user, otp=user_otp)
                # messages.info(request, "Hello {user.first_name},\n Your OTP is {user_otp}\n Thanks!"
                messages.info(request,'Register successfully')
                return render(request, 'login.html')
                # return render(request, 'messages.html')
        else:
            messages.info(request,'Password not match')
            return redirect('/register')

    else:
        return render(request,'register.html')

def Login (request):
    if request.method=='POST':
        username=request.POST['username']  
        password=request.POST['password1']
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            messages.info(request,'Login Successfully')
            return redirect('post')
        else:
            messages.info(request,'Invalid Username & Password')
            return redirect('/login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

