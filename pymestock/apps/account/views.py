from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User

def register_user(request):
    if request.method == 'GET':
        return render(request, "account/signup.html")

    elif request.method == 'POST':
        username = request.POST['floatingUsername']
        password = request.POST['floatingPassword']

        User.objects.create_user(username=username, password=password)

        return HttpResponseRedirect('/login')

def login_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard')

    if request.method == 'GET':
        return render(request, "account/login.html")

    if request.method == 'POST':
        username = request.POST['login-username']
        password = request.POST['login-pwd']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/dashboard')
        else:
<<<<<<< HEAD
            return HttpResponseRedirect('/login')
=======
            return HttpResponseRedirect('/error')
>>>>>>> 562f419e879928beab7d74900c4b2217ba373fc6

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login')

def dashboard(request):
<<<<<<< HEAD
    
    return render(request, "account/dashboard.html", {})
=======
    if request.user.is_authenticated:
        return render(request, "account/dashboard.html", {})
    else:
        return HttpResponseRedirect('/login')

def error(request):
    return render(request, "account/error.html", {})
>>>>>>> 562f419e879928beab7d74900c4b2217ba373fc6
