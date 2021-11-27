from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User
from ..business.models import Business


def register_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/dashboard")

    if request.method == 'GET':
        return render(request, "account/signup.html")

    elif request.method == 'POST':
        username = request.POST['floatingUsername']
        password = request.POST['floatingPassword']
        business = request.POST['floatingBusiness']

        new_business = Business(business_name=business)
        new_business.save()
        last_id = Business.objects.latest('id')

        User.objects.create_user(username=username, password=password, business=last_id, is_owner=True)

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
            return HttpResponseRedirect('/error')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login')


def dashboard(request):
    if request.user.is_authenticated:
        business = Business.objects.get(id=request.user.business.id)
        user = request.user
        return render(request, "account/dashboard.html", {"business": business, "user": user})
    else:
        return HttpResponseRedirect('/login')


def error(request):
    return render(request, "account/error.html", {})


def add_observer(request):
    if not request.user.is_owner:
        return HttpResponseRedirect("/dashboard")

    if request.method == "GET":
        return render(request, "account/worker/signup.html")

    if request.method == "POST" and request.user.is_authenticated:
        if "AddObserver" in request.POST:
            username = request.POST['floatingUsername']
            password = request.POST['floatingPassword']
            business = Business.objects.get(id=request.user.business.id)

            User.objects.create_user(username=username, password=password, business=business)

            business = Business.objects.get(id=request.user.business.id)
            user = request.user
            return render(request, "account/dashboard.html", {"business": business, "user": user})
    else:
        return HttpResponseRedirect('/login')
