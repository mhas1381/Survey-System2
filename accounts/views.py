from django.shortcuts import render
from django.shortcuts import render,redirect
from accounts.urls import *
from django.contrib.auth import authenticate, login,logout
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/survey')
        

    return render(request, 'accounts/login.html')
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/') 