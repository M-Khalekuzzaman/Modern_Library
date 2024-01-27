from django.shortcuts import render,redirect
from accounts.forms import UserRegistrationForm,UpdateUserInfoForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from .models import UpdateUserInfoModel

def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request,'Succeefully Account Created !')
            return redirect('login_page')
        
    else:
        form = UserRegistrationForm()
    return render(request,'registration_page.html',{'form':form})

def logIn(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            userpassword = form.cleaned_data['password']
            user = authenticate(username = username,password = userpassword)
            
            if user is not None:
                login(request,user)
                return redirect('profile_page')
            
    else:
        form = AuthenticationForm()
    return render(request,'login_page.html',{'form':form})

def profile(request):
  if request.user.is_authenticated:
    return render(request,'profile_page.html',{'user':request.user})
  else:
    return redirect('login_page')

def logOut(request):
    logout(request)
    return redirect('home_page')

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user = request.user,data = request.POST)
        if form.is_valid():
            form.save(commit=True)
            update_session_auth_hash(request,form.user)
            return redirect('login_page')
            
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request,'change_password.html',{'form':form})

def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html',{'user':request.user})
    else:
        return redirect('login_page')
    
def change_password_without_oldpass(request):
    if request.method == "POST":
        form = SetPasswordForm(user = request.user,data = request.POST)
        if form.is_valid():
            form.save(commit=True)
            update_session_auth_hash(request,form.user)
            return redirect('login_page')
            
    else:
        form = SetPasswordForm(user = request.user)
    return render(request,'change_password.html',{'form':form})

def user_update_info(request):
    if request.method == 'POST':
        form = UpdateUserInfoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    else:
        form = UpdateUserInfoForm()
    return render(request,'edit_profile.html',{'form':form})
 
        