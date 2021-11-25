from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User

def register_user(request):
    if request.method == 'GET':
        return render(request, "account/signup.html")

    elif request.method == 'POST':
        print(request.POST)
        username = request.POST['floatingUsername']
        password = request.POST['floatingPassword']

        user = User.objects.create_user(username=username, password=password)

        return HttpResponseRedirect('/login')

def login_user(request):
    if request.method == 'GET':
        print('a')
        return render(request, "account/login.html")

    if request.method == 'POST':
        username = request.POST['login-username']
        password = request.POST['login-pwd']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/dashboard')
        else:
            print('a')
            return HttpResponseRedirect('login.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('login.html')

def dashboard(request):
    return render(request, "account/dashboard.html", {})
