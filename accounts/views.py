from django.shortcuts import render,redirect
from django.contrib.auth import login , logout,authenticate
# Create your views here.
def login_page(request):
    return render(request, 'accounts/login.html')
def logged_in(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request,'survey/survey.html')