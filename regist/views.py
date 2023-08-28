from django.shortcuts import render,redirect
from django.contrib.auth.models import User #for connect the view to admin it save user data in admin   
from django.contrib.auth import authenticate,login,logout#for varify the signup password to match the login username password also logout for use logout form page
from django.contrib.auth.decorators import login_required
#for first visit the user on login not the home page without login

def signUp(self):
    if self.method=='POST':
        name=self.POST.get("username")
        Email=self.POST.get("email")
        password=self.POST.get("password")
        password1=self.POST.get("password1")
        if password!=password1:
            return render(self,"signup.html",{'error':True})
        else:
            my_user=User.objects.create_user(name,Email,password)
            my_user.save()
            return redirect("login")
    return render(self,"signup.html")

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get("username")
        passwords=request.POST.get("password")
        user=authenticate(request,username=username,password=passwords)
        #user variable is use to find the username and password check in signin and login form it same or not
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,"login.html",{'errors':True})
    return render (request,"login.html")
#login_required most be on home page 
@login_required(login_url='login')
def home(self):
    return render(self,"home.html")
def logouts(request):
    logout(request)
    return redirect('login')
# Create your views here.
