from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Signup view
def sign_up(request):
    if request.method == "POST":
     fm=SignUpForm(request.POST)
     if fm.is_valid():
         messages.success(request,'Account Created Successfully!!')
         fm.save()
    else:
     fm=SignUpForm()
    return render(request,'html/signup.html',{'form':fm})

#Login view
def user_login(request):
    if request.method == 'POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user= authenticate(username=uname, password=upass)
            if user is not None:
                login(request,user)
                return
    fm =AuthenticationForm()
    return render(request,'html/userlogin.html' ,{'form':fm})
